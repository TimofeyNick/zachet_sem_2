S = input()
N = len(S)
z = [0]*N
for i in range(1, N):
    x = 0
    while i + x < N and S[x] == S[i+x]:
        x += 1
    z[i] = x

print(z)