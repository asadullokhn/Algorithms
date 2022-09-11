o = input
l, p = map(int, o().split())
n = set(o().split())
for i in range(p):
    print(['NO', 'YES'][o() in n])
