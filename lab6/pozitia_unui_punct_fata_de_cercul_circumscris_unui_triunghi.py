def criteriu_numeric(a, b, c, d):
    diag_p = (b[0] - a[0]) * (c[1] - a[1]) * (d[0] * d[0] + d[1] * d[1] - a[0] * a[0] - a[1] * a[1])
    p1 = (c[0] - a[0]) * (d[1] - a[1]) * (b[0] * b[0] + b[1] * b[1] - a[0] * a[0] - a[1] * a[1])
    p2 = (d[0] - a[0]) * (b[1] - a[1]) * (c[0] * c[0] + c[1] * c[1] - a[0] * a[0] - a[1] * a[1])
    
    diag_s = (d[0] - a[0]) * (c[1] - a[1]) * (b[0] * b[0] + b[1] * b[1] - a[0] * a[0] - a[1] * a[1])
    s1 = (c[0] - a[0]) * (b[1] - a[1]) * (d[0] * d[0] + d[1] * d[1] - a[0] * a[0] - a[1] * a[1])
    s2 = (d[1] - a[1]) * (b[0] - a[0]) * (c[0] * c[0] + c[1] * c[1] - a[0] * a[0] - a[1] * a[1])
    
    return - (diag_p + p1 + p2 - diag_s - s1 - s2)


a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

n = int(input())

rez = []
for i in range(n):
    pct = [int(x) for x in input().split()]
    
    crit = criteriu_numeric(a, b, c, pct)
    if crit > 0:
        rez.append("INSIDE")
    elif crit == 0:
        rez.append("BOUNDARY") 
    else:
        rez.append("OUTSIDE")

for r in rez:
    print(r)
    