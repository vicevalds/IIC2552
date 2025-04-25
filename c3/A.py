n = int(input())
l = []
for _ in range(n):
    name = input()
    if name not in l:
        l.append(name)
        print("NO")
    else:
        print("YES")
