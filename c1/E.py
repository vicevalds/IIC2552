n, s = ( int(e) for e in input().split() )
l = [ int(e) for e in input().split() ]
l.sort()

med = int(len(l)/2)
dulces = 0
if l[med] < s:
    l = l[med:]
    for a in l:
        if a < s:
            dulces += s - a
        else:
            break
else:
    l = l[:med+1][::-1]
    for a in l:
        if a > s:
            dulces += a - s
        else:
            break
print(dulces)
