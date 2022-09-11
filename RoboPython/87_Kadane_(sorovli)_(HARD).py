y = lambda: map(int, input().split())
l, q = y()
a = list(y())
for _ in range(q):
    k, x = y()
    a[k - 1] = x
    t = m = a[0]
    for i in range(1, l):
        m = max(a[i], m + a[i])
        t = max(t, m)
    print(t)
