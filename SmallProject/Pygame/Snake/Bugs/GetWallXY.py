a = []
b = []
c = []
for i in range (0, 761):
    if i % 40 == 0:
        a.append(i)
for i in range (0   , 561):
    if i % 40 == 0:
        b.append(i)
for x in a:
    for y in b:
        c.append([x, y])
for i in range(0, len(c)):
    print(c[i])