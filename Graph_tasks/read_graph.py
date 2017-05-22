def read_graph_as_matrix():
    N, M = map(int, input().split())
    W = [[0]*N for i in range(N)]
    for i in range(M):
        a, b = map(int,input().split())
        W[a][b] = 1
        #W[b][a] = 1
    for elem in W:
        print(*elem)

def read_graph_as_list_no_orient(): # список смежности
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        #graph[b].append(a)
    print(graph)

def read_graph_as_list_orient(): # словарь словарей
    N, M = map(int, input().split())
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        if a not in G:
            G[a] = {b:weight}
        else:
            G[a][b] = weight
        # if b not in G: # если неориентированный
        #     G[b] = {a: weight}
        # else:
        #     G[b][a] = weight
    print(G)

# 4 4
# 0 1
# 1 2
# 1 3
# 2 3

read_graph_as_matrix()