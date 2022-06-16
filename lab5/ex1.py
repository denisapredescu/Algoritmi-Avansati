# Testul de orientare

# 3
# 1 1 5 3 2 3
# 1 1 5 3 4 1
# 1 1 5 3 3 2


# 1  1   1
# x1 x2 x3
# y1 y2 y3

def determinant( x1, y1, x2, y2, x3, y3):
    return x2 * y3 + x1 * y2 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


t  = int(input())

rez =[]

while t != 0:
    
    x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
    rez_d = determinant(x1, y1, x2, y2, x3, y3)
    print(rez_d)
    if rez_d == 0:
        rez.append("TOUCH")
    elif rez_d > 0:
        rez.append("LEFT")
    else:
        rez.append("RIGHT")
        
    t -= 1
    
for r in rez:
    print(r)
    
