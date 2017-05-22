def read_graph_as_matrix(N, M):
    W = [[0]*N for i in range(N)]
    for i in range(M):
        a, b = map(int,input().split())
        W[a][b] = 1
        #W[b][a] = 1
    for elem in W:
        print(*elem)
    print()
    return W

def get_input_output_degree(N, M, W):
    A = [] # входящая степень вершины
    B = [] # исходящая степень вершины
    for vertex in range(N):
        i = 0
        for j in range(N):
            if W[vertex][j] == 1:
                i += 1
        A.append(i)
    for vertex in range(N):
        i = 0
        for j in range(N):
            if W[j][vertex] == 1:
                i += 1
        B.append(i)
    return A, B

N, M = map(int, input().split())
W = read_graph_as_matrix(N, M)
A, B = get_input_output_degree(N, M, W)
print(' '.join(map(str, A)))
print(' '.join(map(str, B)))