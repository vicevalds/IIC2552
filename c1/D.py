
d, c, r = ( int(n) for n in input().split() )
con = [int(input()) for a in range(c)]
rev = [int(input()) for a in range(r)]

t = 0
d += sum(rev)
t += len(rev)

for a in con:
    if a <= d:
        d -= a
        t += 1
    else:
        break
print(t)
