def read_graph_as_list_no_orient(): # список смежности
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        #graph[b].append(a)
    return graph

def call_all_friends(me, friends, invited):
    invited.add(me)
    for friend in friends[me]:
        if friend not in invited:
            call_all_friends(friend, friends, invited)

graph = read_graph_as_list_no_orient()
invited = set()
number_comp = 0
for friend in range(len(graph)):
    if friend not in invited:
        call_all_friends(friend, graph, invited)
        number_comp +=1

print('number_comp =' , number_comp)

