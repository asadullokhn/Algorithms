n = input()
l = len(n)
p = l // 2
print(n[:p] + n[p - (l % 2 == 0)::-1])