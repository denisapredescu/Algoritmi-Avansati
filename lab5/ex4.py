# Punct în poligon convex

def determinant( x1, y1, x2, y2, x3, y3):
    return x2 * y3 + x1 * y2 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

n = int(input())
p = []  # puncte poligon
output = [] 

for i in range(n):
    x, y = [int(q) for q in input().split()]
    if len(p) >= 2: 
        # tai punctul din mijloc daca am 3 coliniare
        r = determinant(p[len(p)-2][0], p[len(p)-2][1], p[len(p)-1][0], p[len(p)-1][1], x, y)
        if r == 0: 
            p = p[:len(p)-1]
    p.append([x, y])

n = len(p)

# ultimele 2 punct cu primul
r = determinant(p[n-2][0], p[n-2][1], p[n-1][0], p[n-1][1], p[0][0], p[0][1])
if r == 0: # puncte coliniare
    p = p[:n-1]
    n = n - 1
       
# ultimul + primele 2          
r = determinant(p[n-1][0], p[n-1][1], p[0][0], p[0][1], p[1][0], p[1][1])
if r == 0: # puncte coliniare
    p = p[1:]
    n = n - 1
        
m = int(input())
index1 = -1
index2 = -1

while m != 0:    
    right = 0
    left = 0
    touch = 0

    x, y = [int(x) for x in input().split()]
    
    for i in range(n):
        r = determinant(p[i][0], p[i][1], p[(i + 1) % n][0], p[(i + 1) % n][1], x, y)
        if r == 0:
            if touch == 0:
                index1 = i
            else:
                index2 = i 
            touch += 1
        elif r > 0:
            left += 1
        else:
            right += 1
            
        if touch == 2:
            break
        
        if right != 0 and left != 0:
            break
    m -= 1
    
    if left == n:
        output.append("INSIDE")
    elif (touch == 1  and right == 0) or (touch == 2 and (index2 == index1 + 1 or (index2 == n - 1 and index1 == 0))):    # se afla pe latura sau pe vf
        output.append("BOUNDARY")
    else: 
        output.append("OUTSIDE")
        
for rez in output:
    print(rez)