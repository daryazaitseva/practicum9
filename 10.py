def count(a, b):
    if a == 0:
        return 1
    if a < 0 or b == 0:
        return 0
    return count(a - b, b - 1) + count(a, b - 1)

k = int(input())
print(count(k, k))
