s = input()
l = list({ x for x in s })
l.sort()
print(len(s)-len(''.join(l)))
