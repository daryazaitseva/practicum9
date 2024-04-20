n = int(input())
k = 0
for i in range(0, n + 1):
    for j in range(n, i - 1, -1):
        k += i + j
print(k)