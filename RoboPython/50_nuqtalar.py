p = input
s = sorted
r = range
n = int(p())
a = s(map(int, p().split()))
b = s([a[i] - i + 2 for i in r(n)])
print(sum([abs(b[i] - b[n // 2]) for i in r(n)]))
