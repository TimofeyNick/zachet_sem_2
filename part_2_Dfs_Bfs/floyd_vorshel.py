def read_graph():
    N, M = map(int, input().split())
    W = [[float('+inf')]*N for i in range(N)]
    for i in range(N):
        W[i][i] = 0
    for i in range(M):
        a, b, w = map(int, input().split())
        W[a][b] = w
        W[b][a] = w
    return W, N

def floyd_vorshel(W, N):
    INF = float('+inf')
    A = [[[INF]*N for i in range(N)] for k in range(N+1)]
    for i in range(N): #записываем весовую матрицу, как начальную
        A[0][i][:] = W[i]
    for k in range(1, N+1):
        for i in range(N):
            for j in range(N):
                A[k][i][j] = min(A[k-1][i][j], A[k-1][i][k] + A[k-1][k][j])
        for elem in A[k]:
            print(' '.join(map(str, elem)))
    return A[N]

W, N = read_graph()
Weight = floyd_vorshel(W, N)
print(Weight)
