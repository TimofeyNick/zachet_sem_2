s = input()
n = len(s)
z = [0]*n
left = 0
right = 0
for i in range(1,n):
    x = min(z[i-left], right - i + 1) i <=right else 0 
    while x + i < n and s[x] == s[x + i]:
        x += 1
    z[i] = x
    if i + x - 1 > right:
        left, right = i, i + x - 1

print(" ".join(map(str, z)))
