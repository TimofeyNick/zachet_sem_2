def read_graph_as_list(N, M):
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    return graph

def call_all_friends(me, friends, invited):
    invited.add(me)
    for friend in friends[me]:
        if friend not in invited:
            call_all_friends(friend, friends, invited)

def check_degree(bool_1):
    if bool_1 == False:
        return('NO')
    for list_elem in graph:
        if len(list_elem)%2 !=0:
            return('NO')
    return('YES')

# N=vertexes, M=edges
N, M = int(input()), int(input())
graph = read_graph_as_list(N, M)
invited = set()
number_comp = 0
bool_1 = False
for friend in range(N):
    if friend not in invited:
        call_all_friends(friend, graph, invited)
        number_comp += 1

if number_comp == 1:
    bool_1 = True
result = check_degree(bool_1)
print(result)

# 4
# 4
# 0 1
# 1 2
# 2 3
# 3 0

# 3
# 2
# 0 1
# 1 2