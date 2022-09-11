l = input
d = {}
o = int
q = lambda: range(o(l()))
for i in q():
    a, b = l().split()
    t = d.get(a)
    d[a] = t + o(b) if t else o(b)

for i in q():
    e = l()
    print(e, d[e])
