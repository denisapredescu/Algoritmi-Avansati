import heapq

def determinant( x1, y1, x2, y2, x3, y3):
    return x2 * y3 + x1 * y2 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

n = int(input())
h_cresc = []
h_descresc = []
li = []
ls = []

for i in range(n):
    x, y = [int(q) for q in input().split()]
    heapq.heappush(h_cresc, (x, y))

li.append(heapq.heappop(h_cresc))
li.append(heapq.heappop(h_cresc))

while len(h_cresc) != 0:
    
    p = heapq.heappop(h_cresc)
    r = determinant(li[len(li)-2][0], li[len(li)-2][1], li[len(li)-1][0], li[len(li)-1][1], p[0], p[1])

    while r <= 0 and len(li) >= 2 :
        x, y = li[len(li)-1]
        li = li[:len(li)-1]
        
        if r < 0:
            heapq.heappush(h_descresc, (-x, -y))
        
        if len(li) >= 2:
            r = determinant(li[len(li)-2][0], li[len(li)-2][1], li[len(li)-1][0], li[len(li)-1][1], p[0], p[1])
    
        
    li.append(p)
    
primx, primy = li[0]
ultx, ulty = li[len(li) - 1]
heapq.heappush(h_descresc, (-primx, -primy))
heapq.heappush(h_descresc, (-ultx, -ulty))
ls.append(heapq.heappop(h_descresc))
ls.append(heapq.heappop(h_descresc)) 
 
while len(h_descresc) != 0:
    
    p = heapq.heappop(h_descresc)
    r = determinant(ls[len(ls)-2][0], ls[len(ls)-2][1], ls[len(ls)-1][0], ls[len(ls)-1][1], p[0], p[1])
    
    while r <= 0 and len(ls) >=2 :
        x, y = ls[len(ls)-1]
        ls = ls[:len(ls)-1]
        
        if len(ls) >= 2:
            r = determinant(ls[len(ls)-2][0], ls[len(ls)-2][1], ls[len(ls)-1][0], ls[len(ls)-1][1], p[0], p[1])
        
    ls.append(p)


print(len(li) + len(ls) - 2)

for x, y in li:
    print(f"{x} {y}")
    
for x, y in ls[1:len(ls)-1]:
    print(f"{-x} {-y}")