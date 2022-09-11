import math as m

i = input

for _ in range(int(i())):
    *a, c = map(int, i().split())
    print(['YES', 'NO'][c > max(*a) or c % m.gcd(*a) != 0])
