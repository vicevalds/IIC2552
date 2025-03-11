n, s = ( int(e) for e in input().split() )
l = [ int(e) for e in input().split() ]
l.sort()
u = 0
dif = 0
med = int(len(l)/2)
while l[med] != s:
    if l[med] > s:
        dif = l[med] - s
        l[med] -= dif
    else:
        dif = s - l[med]
        l[med] += dif
    u += dif
    l.sort()
print(u)
