p=input
s=print
for _ in range(int(p())):
    n = int(p())

    if n % 2:
        s(0)

    else:
        n /= 2
        c, i = 0, 1

        while i * i <= n:
            if n % i == 0:
                c += 1 + (i != n / i)
            i += 1

        s(c)
