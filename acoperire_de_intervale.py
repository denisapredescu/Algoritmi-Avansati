import heapq

a, b = [int(x) for x in input().split()]

N = int(input())
h = []

for i in range(1, N+1):
    x, y = [int(x) for x in input().split()]
    if not(y <= a or x >= b):
        heapq.heappush(h, (x, y, i))
        
ok = False # devine true cand gasim o solutie

intervale = []

chosen = heapq.heappop(h)

while not(ok) and len(h) > 1 :
    
    chosen = heapq.heappop(h)
    x, y, poz_xy = heapq.heappop(h)
    
    while x <= a  and chosen[0] <= a and len(h) > 0:
        if y > chosen[1]:
            chosen = (x, y, poz_xy)
        
        x, y, poz_xy = heapq.heappop(h)  
    
    if x >= a:
        heapq.heappush(h, (x, y, poz_xy))
    
    if b <= chosen[1]: 
        ok = True
        intervale.append(chosen[2])
            
    elif chosen[1] >= a and chosen[0] <= a:
        a = chosen[1]
        intervale.append(chosen[2])
    
   
if len(h) == 1 :
    x, y, poz_xy = heapq.heappop(h)
    if a >= x  and b <= y:
        ok = True
        intervale.append(poz_xy) 
    
if ok == True:
    print(len(intervale))
    for interv in intervale:
        print(interv, end=" ")
else:
    print(0)
        
        
    
    
