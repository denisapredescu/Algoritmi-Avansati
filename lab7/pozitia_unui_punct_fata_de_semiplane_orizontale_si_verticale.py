n = int(input())

plane = []

while n != 0:
    plane.append([int(i) for i in input().split()])
    n -= 1

# ax + by + c = 0
# x apartine de [min_x, max_x]  => initial [-inf, +inf]
# y apartine de [min_y, max_y]  => initial [-inf, +inf]

m = int(input())
while m != 0:
    x, y = [float(i) for i in input().split()]

    min_x = -float('inf')
    max_x = float('inf')
    min_y = -float('inf')
    max_y = float('inf')
    
    for a, b, c in plane:
        
        # aici b == 0
        if a < 0:
            if x > -c / a and min_x < -c / a:
                min_x = - c / a
        elif a > 0:
            if x < -c / a and  max_x > -c / a:
                max_x = -c / a
        
        # aici a == 0
        if b < 0:
            if y > -c / b and min_y < -c / b:
                min_y = -c / b
        elif b > 0:
            if y < -c / b and  max_y > -c / b:
                max_y  = -c / b
                    
    if min_x <= x <=  max_x and min_y <= y <= max_y:
        if not(min_x == -float('inf') or max_x == float('inf') or min_y == -float('inf') or max_y == float('inf')):
            print("YES")
            print((max_x - min_x) * (max_y - min_y))
        else:
            print("NO")
    else:
        print("NO")
    
    m -= 1
    

 
    
# 5
# 1 0 -1
# -1 0 -1
# 0 1 -2
# 0 -1 -2
# 0 -1 -3
# 4
# 2 0
# 1 0
# 0 0
# 0 -2.5