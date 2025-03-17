import math

n, q = ( int(e) for e in input().split() )
ln = [ int(a) for a in input().split() ]

ones = [ n if n == 1 else 0 for n in ln ]
# https://python.19633.com/es/Python/1002008321.html
# como saber si es potencia de 2 en python3
even = [ n if math.log(n,2).is_integer() and n != 1 else 0 for n in ln ]
odd = [ n if n%2 != 0 and n != 1 else 0 for n in ln ]
for _ in range(q):
    l, r = ( int(e) - 1 for e in input().split() )
    s = sum(ones[l:r+1])/2
    agu = math.ceil(s) + sum(even[l:r+1])
    bri = math.floor(s) + sum(odd[l:r+1])
    if agu > bri:
        print("A")
    elif agu < bri:
        print("B")
    else:
        print("E")
