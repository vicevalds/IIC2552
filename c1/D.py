from collections import deque

d, c, r = ( int(n) for n in input().split() )
con = deque(sorted([int(input()) for a in range(c)]))
rev = deque(sorted([int(input()) for a in range(r)], reverse=True))

t = 0
while d >= 0 and len(rev) > 0:
    print(f"energia actual {d}")
    print(f"tareas listas {t}")
    print(f"con {con}")
    print(f"rev {rev}")
    if len(con) > 0 and d - con[0] >= 0:
        v = con.popleft()
        print(f"menos {v}")
        d -= v
    else:
        rr = rev.popleft()
        d += rr
        print(f"mas {rr}")
    t += 1
#print(t)
print(f"energia actual {d}")
print(f"tareas listas {t}")
print(f"con {con}")
print(f"rev {rev}")
