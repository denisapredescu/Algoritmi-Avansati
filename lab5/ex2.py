# Roby

# 1  1   1
# x1 x2 x3
# y1 y2 y3

def determinant( x1, y1, x2, y2, x3, y3):
    return x2 * y3 + x1 * y2 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


n  = int(input())

rez =[]
p = []

right = 0
left = 0
touch = 0
for i in range(n):
    p.append([int(x) for x in input().split()])
    
for i in range(n - 1):
    r = determinant(p[i][0], p[i][1], p[(i + 1) % n][0], p[(i + 1) % n][1], p[(i + 2) % n][0], p[(i + 2) % n][1])
    if r == 0:
        touch += 1
    elif r > 0:
        left += 1
    else:
        right += 1

print(left, right, touch)
    
