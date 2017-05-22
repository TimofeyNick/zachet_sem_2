def read_graph_as_matrix():
    N, M = map(int, input().split())
    W = [[0]*N for i in range(N)]
    for i in range(M):
        a, b = map(int,input().split())
        W[a][b] = 1
        #W[b][a] = 1
    for elem in W:
        print(*elem)
    print_dopolnenie(N, M, W)

def print_dopolnenie(N, M, W):
    for i in range(N):
        for j in range(N):
            if W[i][j] == 0:
                print(i, j)

read_graph_as_matrix()

