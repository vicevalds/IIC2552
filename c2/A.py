n, q = ( int(e) for e in input().split() )
lg = [ int(e) for e in input().split() ]
lq = [ int(e) for e in input().split() ]

for q in lq:
    l = 0
    r = len(lg)
    while l < r:
        i = (l + r)//2
        if lg[i] <= q:
            l = i + 1
        else:
            r = i
    print(l, end=" ")
