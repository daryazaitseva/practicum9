n = int(input())
k = 0
for i in range(0, n + 1):
    for j in range(0, n + 1):
        if i != j:
            k += i + j
print(k)