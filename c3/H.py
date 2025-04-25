#n, k = (int(e) for e in input().split())
#lpkm = [int(e) for e in input().split()]
n,k = (5, 2)
lpkm = ["A", 4, 5, 3, "A"]

#turn = 0
#while 0 in catch:
print(k)
print(lpkm)
pkm = max(lpkm)
print(pkm)
#    if turn%2 == 0:
pkm_index = lpkm.index(pkm)
print(pkm_index)
count = pkm_index - k
while pkm != "A" and count <= 2*k:
    lpkm[count] = "H"
    count += 1
    print(lpkm)

"""
5 2
2 4 5 3 1

2 X X X 1
A 4 5 3 X
"""
