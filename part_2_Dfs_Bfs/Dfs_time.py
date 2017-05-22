def read_graph_as_list_no_orient(): # список смежности
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        #graph[b].append(a)
    return graph

def call_all_friends(me, friends, invited, Times, time):
    invited.add(me)
    Time[me] = time
    for friend in friends[me]:
        if friend not in invited:
            call_all_friends(friend, friends, invited, Times, time + 1)
    return Time

graph = read_graph_as_list_no_orient()
Time = [None for i in range(len(graph) + 1)]
invited = set()
start = 3
Time = call_all_friends(start, graph, invited, Time, 0)
for u,v in enumerate(Time):
    print(u, ':' , v)