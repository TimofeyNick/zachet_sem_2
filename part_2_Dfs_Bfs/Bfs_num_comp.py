def read_graph_as_list_no_orient(): # список смежности
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        #graph[b].append(a)
    return graph

def bfs(start, graph, fired):
    Queue = [start]
    fired.add(start)
    while len(Queue)!= 0:
        cur = Queue.pop(0)
        for neig in graph[cur]:
            if neig not in fired:
                fired.add(neig)
                Queue.append(neig)

graph = read_graph_as_list_no_orient()
fired = set()
num_comp = 0
for vertex in range(len(graph)):
    if vertex not in fired:
        bfs(vertex, graph, fired)
        num_comp += 1

print(num_comp)
