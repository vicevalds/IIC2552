n, s = ( int(e) for e in input().split() )
l = [ int(e) for e in input().split() ]
l.sort()
u = 0
dif = 0
while l[int(len(l)/2)] != s:
    if l[int(len(l)/2)] > s:
        dif = l[int(len(l)/2)] - s
        l[int(len(l)/2)] -= dif
    elif l[int(len(l)/2)] < s:
        dif = s - l[int(len(l)/2)]
        l[int(len(l)/2)] += dif
    u += dif
    l.sort()
print(u)
