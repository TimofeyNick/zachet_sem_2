first = input()
second = input()
l_first, l_second = len(first), len(second)
matrix = [[0]*(l_first + 1) for i in [0]*(l_second + 1)]

for i in range(1, len(first) + 1):
    matrix[0][i] = i
for j in range(1, len(second) + 1):
    matrix[j][0] = j

for i in range(1, len(second) + 1):
    for j in range(1, len(first) + 1):
        matrix[i][j] = min(
            matrix[i-1][j] + 1,
            matrix[i][j-1] + 1,
            matrix[i-1][j-1] + (0 if first[j-1] == second[i-1] else 1))

print(matrix[l_second][l_first])