n = input()
if n == '10':
    print(9)
else:
    q = len
    l = q(n)
    i = int
    t = l % 2 == 0
    j = l // 2
    f = lambda: n[:j] + n[j - t::-1]
    p = f()
    if i(p) > i(n):
        n = str(i(p[:q(p) // 2 + (not t)]) - 1)
        print([f(), n * 2][l == 1])
    else:
        print(p)
