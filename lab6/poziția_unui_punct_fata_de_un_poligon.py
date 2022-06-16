def determinant( x1, y1, x2, y2, x3, y3):
    return x2 * y3 + x1 * y2 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

def nr_intersectii(qxy, p1, p2):
    
    rez_d1 = determinant(p1[0], p1[1], p2[0], p2[1], qxy[0], qxy[1])   # p1 p2 pct
    rez_d2 = determinant(p1[0], p1[1], p2[0], p2[1], Mx, My)   # p1 p2 M
    rez_d3 = determinant(Mx, My, qxy[0], qxy[1], p1[0], p1[1])   # M pct p1
    rez_d4 = determinant(Mx, My, qxy[0], qxy[1], p2[0], p2[1])   # M pct p2
    
    if (rez_d1 >= 0 and rez_d2 <= 0) or (rez_d1 <= 0 and rez_d2 >= 0):  # M i qxy se afla de o parte si de alta a dreptei p1 - p2
        if (rez_d3 >= 0 and rez_d4 <= 0) or (rez_d3 <= 0 and rez_d4 >= 0): 
                return 1    
    return 0


def onBorder(qxy, p1, p2):
    if determinant(p1[0], p1[1], p2[0], p2[1], qxy[0], qxy[1]) == 0:
        if p1[0] <= qxy[0] <= p2[0] or p1[0] >= qxy[0] >= p2[0]: 
            if p1[1] <= qxy[1]<= p2[1] or p1[1] >= qxy[1] >= p2[1]: 
                return 1
    return 0


n = int(input())

p = []
for i in range(n):
    xy = [int(x) for x in input().split()]
    p.append((xy[0], xy[1]))      

    
m = int(input())   # nr de puncte

rez = []
for k in range(m):
    q = [int(x) for x in input().split()]

    Mx = 9999999999   # iau un numar exterior pe care sa formeze un segment (q, M) putin inclinat 
    My = q[1] + 5   
    contor = 0
    border = 0
    
    for i in range(n-1):
        contor += nr_intersectii(q, p[i], p[i+1])
        border += onBorder(q, p[i], p[i+1])
        
    contor += nr_intersectii(q, p[n-1], p[0])
    border += onBorder(q, p[n-1], p[0])
    
    if border != 0:
        rez.append("BOUNDARY")
    elif contor % 2 == 0: # q in exterior
        rez.append("OUTSIDE")
    else:               # INSIDE 
        rez.append("INSIDE")
        
for r in rez:
    print(r)
    
    
# 12
# 0 6
# 0 0
# 6 0
# 6 6
# 2 6
# 2 2
# 4 2
# 4 5
# 5 5
# 5 1
# 1 1
# 1 6
# 3
# 3 5
# 7 3
# 3 2


