for i in range(100000, 999999 + 1):
    if str(i) == str(i)[::-1]:
        i = i - 1
        if str(i)[1:5] == (str(i)[1:5])[::-1]:
            i = i - 1
            if str(i)[1::] == (str(i)[1::])[::-1]:
                i = i - 1
                if str(i)[1::] == (str(i)[1::])[::-1]:
                    print(i)
