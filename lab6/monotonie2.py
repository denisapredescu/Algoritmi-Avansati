n = int(input())

p = []
for i in range(n):
    xy = [int(x) for x in input().split()]
    p.append([xy[0], xy[1]])
    
def isMonotone(coordinate):
    if coordinate == "x":
        j = 0
    else: 
        j = 1
        
    coordinate_smaller_then_neighbors = 0
    for i in range(0, n):
        if p[i][j] < p[(i+1) %n][j] and p[i][j] < p[(i-1) %n][j]:
            coordinate_smaller_then_neighbors += 1
    return (coordinate_smaller_then_neighbors == 1)

if isMonotone("x") == True:
    print("YES")
else:
    print("NO")
    
if isMonotone("y") == True:
    print("YES")
else:
    print("NO")

    
