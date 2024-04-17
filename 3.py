n = int(input())
if n % 2 == 0 and n >= 2:
    print(2)
else:
    k = []
    for i in range(3, n // 2 + 1):
        if n % i == 0:
            k.append(i)
    if len(k) == 0:
        print('невозможно')
    else:
        print(k[0])
