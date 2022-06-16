import heapq
from math import expm1
from os import uname

def citire():
    f = open("ex1.in")
    n = int(f.readline())
    greutate = [int(x) for x in f.readline().split()]
    valoare = [int(x) for x in f.readline().split()]
    cantitate = int(f.readline())
    return n, cantitate, greutate, valoare

# O(n)
def creareTupluri():
    h = []
    for i in range(n):
        heapq.heappush(h, (greutate[i]/valoare[i], greutate[i], valoare[i]))
    return h

n, cantitate, greutate, valoare = citire()
h = creareTupluri()

# maxim O(nlogn)
val = 0
while cantitate != 0 and len(h) != 0:
    elem = heapq. heappop(h)

    if cantitate < elem[1]:
        valF = cantitate * (elem[2] /  elem[1])
        print(f"Greutate totala {elem[1]}, valoare totala {elem[2]}; Greutate fractionata {cantitate}, valoare {valF}")
        cantitate = 0
        val += valF
    else:
        val += elem[2]
        print(f"Greutate {elem[1]}, valoare {elem[2]}")
        cantitate -= elem[1]

print(f"Profit = {val}")


# in cazul in care nu putem fractiona un sac, strategia ramane aceeasi adica folosesc un heap si le 
# sortez in functie de raportul greutate/valoare; diferenta este la calculul profitului => ne oprim 
# cand ajungem la cazul in care cantitate < elem[1], astfel incat nu mai introducem o portiune intr-un
# sac. Solutie? Ca si in algoritmul creat, cantitate = 0, deci se va opri while-ul.




