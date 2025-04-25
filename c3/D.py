n = int(input())
p = [int(e) for e in input().split()]
a = [int(e) for e in input().split()]
b = [int(e) for e in input().split()]
m = int(input())
c = [int(e) for e in input().split()]

d = { p[i]: (a[i], b[i]) for i in range(n) }
# https://stackoverflow.com/questions/9860588/maximum-value-for-long-integer
for e in c:
    mm = float("inf")
    for k, v in d.items():
        #print(k, v)
        if e in v and k < mm:
            #print(c, v, k, mm)
            mm = k
            #print(mm)
    if mm == float("inf"):
        print(-1)
        break
    print(mm, end=" ")
    try:
        del d[mm]
    except Exception:
        print(-1)
        break
