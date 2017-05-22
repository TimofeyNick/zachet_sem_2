def read_graph_as_matrix(N, M):
    W = [[0]*N for i in range(N)]
    for i in range(M):
        a, b = map(int,input().split())
        W[a][b] = 1
        #W[b][a] = 1
    for elem in W:
        print(*elem)
    return W

def get_degree_from_matrix(N, M, W):
    A = []
    for vertex in range(N):
        i = 0
        for j in range(N):
            if W[vertex][j] == 1:
                i += 1
        A.append(i)
    return A

N, M = map(int, input().split())
W = read_graph_as_matrix(N, M)
A = get_degree_from_matrix(N, M, W)
print(' '.join(map(str, A)))