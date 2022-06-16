n = int(input())

min_x = -float('inf')
max_x = float('inf')
min_y = -float('inf')
max_y = float('inf')

# x apartine de [min_x, max_x]  => initial [-inf, +inf]
# y apartine de [min_y, max_y]  

while n!=0:
    x, y, rez = [int(i) for i in input().split()]
    
    if x < 0:
        if min_x < rez:
            min_x = rez
    elif x > 0:
        if max_x > -rez:
            max_x = -rez
    
    if y < 0:
        if min_y < rez:
            min_y = rez
    elif y > 0:
        if max_y > -rez:
            max_y = -rez
                           
    n -= 1


if min_x <= max_x and min_y <= max_y:
    if min_x == -float('inf') or max_x == float('inf') or min_y == -float('inf') or max_y == float('inf'):
        print("UNBOUNDED")
    else:
        print("BOUNDED")
else:
    print("VOID")
    
    

    