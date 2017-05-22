def read_graph_as_list_no_orient(): # список смежности
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        #graph[b].append(a)
    return graph

def bfs_time(start, graph, fired):
    Queue = [start]
    fired.add(start)
    time = {start: 0}
    while len(Queue) != 0:
        cur = Queue.pop(0)
        for neig in graph[cur]:
            if neig not in fired:
                fired.add(neig)
                Queue.append(neig)
                time[neig] = time[cur] + 1
    return time

graph = read_graph_as_list_no_orient()
start = 1
fired = set()
time = bfs_time(start, graph, fired)
sorted(time)
for u in time:
    print(u, ':' , time[u])

# 5 4
# 0 1
# 1 2
# 1 3
# 2 3

# def bfs_time(start, graph, fired):
#     Queue = [start]
#     fired.add(start)
#     while len(Queue)!= 0:
#         cur = Queue.pop(0)
#         for neig in graph[cur]:
#             if neig not in fired:
#                 fired.add(neig)
#                 Queue.append(neig)