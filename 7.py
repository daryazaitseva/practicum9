for a in range(1000, 9999 + 1):
    for b in range(1000, 9999 + 1):
        if ((a // 100) % 10) == (b % 10):
            res = a + b
            A, B = str(a), str(b)
            if 9999 < res < 100000:
                RES = str(res)
                if RES[0] == B[0] and RES[1] == RES[1] and RES[2] == A[2] and RES[3] == B[3]:
                    print(f'{a} + {b} = {res}')
