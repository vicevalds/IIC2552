n, m = (int(e) for e in input().split())
nd = {}
for _ in range(n):
    name, ip = input().split()
    nd[ip] = name
for _ in range(m):
    cmd, ip = input().strip(";").split()
    print(f"{cmd} {ip}; #{nd[ip]}")
