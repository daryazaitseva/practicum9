n = int(input())
s = []
k = 0
s.append(n)
while n != 0:
    n = int(input())
    s.append(n)
for i in range(0, len(s) - 1):
    if s[i] % 4 == 0:
        k += 1
print(k)
