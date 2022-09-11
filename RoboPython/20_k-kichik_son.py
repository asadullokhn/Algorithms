p = input
p()
print(sorted(map(int, p().split()))[int(p()) - 1])
