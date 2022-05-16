#Drawing xmass tree with unnecessarily complicated while loops - Hello rookie!

x=0
while True:
    q = '!' * (1+x)
    p = q.center(100)
    print(p)
    if x < 15:
        x += 4
        continue
    break

x=3
while True:
    q = '!' * (1+x)
    p = q.center(100)
    print(p)
    if x < 25:
        x += 4
        continue
    break

x=3
while True:
    q = '!' * (1+x)
    p = q.center(100)
    print(p)
    if x < 34:
        x += 6
        continue
    break

x=1
while True:
    q = '!' * 4
    p = q.center(100)
    print(p)
    if x < 5:
        x += 1
        continue
    break

q = '!' * 100
p = q.center(100)
print(p)