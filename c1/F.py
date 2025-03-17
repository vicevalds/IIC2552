t = int(input())
for _ in range(t):
    n = int(input())
    al = [ int(n) for n in input().split() ]

    l = [0]
    for i in range(len(al)):
        if i%2 != 0:
            l.append(l[-1] - al[i])
        else:
            l.append(l[-1] + al[i])
    if len(l) != len(set(l[0:])):
        print("YES")
    else:
        print("NO")
