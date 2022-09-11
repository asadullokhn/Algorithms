o = {
    '1': 'bir', '2': 'ikki', '3': 'uch',
    '4': "to'rt", '5': 'besh', '6': 'olti', '7': 'yetti',
    '8': 'sakkiz', '9': 'to\'qqiz', '10': 'o\'n', '20': 'yigirma',
    '30': 'o\'ttiz', '40': 'qirq', '50': 'ellik', '60': 'oltmish',
    '70': 'yetmish', '80': 'sakson', '90': 'to\'qson',
    '00': 'yuz',
    2: 'ming',
    3: 'million',
    4: 'milliard'
}
d = len
n = input()

ns = [n[i - 3: i: 1] for i in range(d(n), 0, -3)]
if d(n) % 3:
    ns[-1] = n[:d(n) % 3]
    
r = []
l = d(ns)
count = 0
for i in ns[::-1]:
    if d(i) > 2:
        if i[-3] != '0':
            r.append(o.get(i[-3]) + " yuz")

    if d(i) > 1:
        if i[-2] != '0':
            r.append(o.get(str(int(i[-2]) * 10)))

    if i[-1] != '0':
        r.append(o.get(str(i[-1])))

    if l - count > 1:
        r.append(o.get(l - count))

    count += 1

print(" ".join(r))
