import math

# 1) citirea oraselor
def citire(fisier):
    f = open(fisier)
    puncte = []
    
    n = int(f.readline())
    for i in range(n):
        x, y = [int(i) for i in f.readline().split()]
        puncte.append([x,y])
    
    f.close()
    return n, puncte

n, puncte = citire("ex1.in")
print(n, puncte)


# 2) distanta euclidiana
def distanta_euclidiana(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3)


d = distanta_euclidiana(puncte[0], puncte[1])
print(d)   



# 3) se creeaza graful complet => matrice de adiacenta; nodurile incep de la 0
def complet(n, puncte):
    
    la = []
    for i in range(n):
        muchii = []
        for j in range(n): 
            if j != i:
                muchii.append([j, distanta_euclidiana(puncte[i], puncte[j])])
                
        la.append(muchii)
    return la


la = complet(n, puncte)
for i in la:
    print(i)


# 4)
solutie = [0 for i in range(n)]
ccurent = 0
cmin = float('inf')

def permute(a, l, r):
    
    global cmin
    
    if l==r:   #s-a creat o solutie
        # print(a)
        ccurent = 0
        i = 0
        while i < len(a) - 1:
            for nod, d in la[a[i]]:
                
                if nod == a[i+1]:
                    # print(a[i], nod, d)
                    ccurent = round(ccurent + d, 3)
                    break  
            i += 1
        
        for nod, d in la[a[0]]:   #inchid ciclul
                
                if nod == a[len(a)-1]:
                    ccurent = round(ccurent + d, 3)
                    break
                
        if ccurent < cmin:
            cmin = ccurent   
            
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 


def startpoint(x):
    v = [x]
    for i in range(n):
        if i != x:
            v.append(i)
            
    return v

v = startpoint(2)
permute(v, 1, n-1)

print(f"Costul minim: {cmin} ")



print()
print("5.")
# 5
solutie = [0 for i in range(n)]
viz = [0 for i in range(n)]
cmin = 0


def distanta_minima(a, l, r):
    
    global cmin
    
    if l==r:
        print(a)
         
        for nod, d in la[a[0]]:   #inchid ciclul 
            if nod == a[len(a)-1]:
                cmin = round(cmin + d, 3)
                break  
            
    else:
        minim = float('inf')
        
        for nod, d in la[a[l]]:   
            if d < minim and viz[nod] == 0:
                minim = d
                newnode = nod
                    
        a[l+1] = newnode
        viz[newnode] = 1
        cmin += minim   
        
        distanta_minima(a, l+1, r)
 
 
def startpoint(x):
    v[0] = x
    viz[x] = 1
    
v = [0 for i in range(n)]
startpoint(2)

distanta_minima(v, 0, n-1)
print(f"Distanta minima: {cmin} plecand din nodul {v[0]}")


# 6 FOLOSESC KRUSKAL
print()
print("6.")
#doar pe neorientate

def citire(fisier): 
    f=open(fisier) #open(numefisier)
    n,m=[int(x) for x in f.readline().split()]
    lm = []  #lista de muchii

    #doua noduri au aceeasi culoare daca au acelas reprezentant => nu ne pasa muchia cum este scrisa
    #pentru noi [n1,n2,c] == [n2,n1,c]

    for i in range(m):
        m1,m2,c= [float(x) for x in f.readline().split()]
        lm.append([int(m1),int(m2),c])
    f.close()
    return n,m,lm

def comp(x):    #pt sortare
    return x[2]

def intializare(i): #varful i formeaza un arbore (o componenta/o multime)
    tata[i] = 0
    h[i] = 0

def reprez(u):    #determin reprezentantul nodului u    
    if tata[u] == 0:
        return u

    # compresie de cale
    tata[u] = reprez(tata[u])   #fac mai usoara determinarea tatalui (ca sa fac arborele mai mic in h => mai usor de parcurs)
    return tata[u]     

# reuniune ponderata
def reuneste(u,v):
    ru=reprez(u)
    rv=reprez(v)
    if h[ru]>h[rv]:
        tata[rv]=ru
    else:
        tata[ru]=rv
        if h[ru] == h[rv]:   #inaltimea se modifica doar daca cei 2 arbori au aceeasi inaltime. de ce? pt ca altfel arborele mai mic devine subarbore arborelui mai mare => nu se modifica h
            h[rv] += 1


adj = [[] for i in range(n)]

def creare_arb(u,v):
    adj[u].append(v)
    adj[v].append(u)
    
    
def kruskal():
    
    lm.sort(key=comp)  
    
    for i in range(1,n+1): #initializaz tata si h pentru fiecare componenta
        intializare(i)

    nr_muchii = 0 #tin evindenta numarului de muchii selectate pentru ca sa opresc algoritmul cand ajung la (n-1)
    
    for u, v, c in lm: 
        if reprez(u) != reprez(v):  #reprezentantul nu va fi niciodata 0, ci daca este vorba doar de un nod, el va fi reprezentantul sau
            reuneste(u, v)
            
            # subpunctul b
            creare_arb(u,v)
            
            # print(u, v, c)
            
            nr_muchii += 1
            if nr_muchii == n-1:
                return
        

def constructieRetea(file):
    f = open(file, "w")
    
    f.write(f"{n} {n * (n-1)}\n")
    
    for i in range(0, n):
        for nod, d in la[i]:
            f.write(f"{i} {nod} {d}\n")

    f.close()


constructieRetea("kruskal.in")    
n,m,lm = citire("kruskal.in")
    
tata=[0 for i in range(n+1)]
h=[0 for i in range(n+1)]


# b) am creat la a) arborele de cost minim cu Kruskal => se gaseste in lista de adiacenta adj graful orientat
    
# for i in adj:
#     print(i)


# test de pe link 14
# adj = [[] for i in range(n)]
# creare_arb(0,1)
# creare_arb(1,2)
# creare_arb(1,3)

# 1 2 3 2 4 2 1
# 0 1 2 1 3 1 0


# c) => parcurgere in adancime pe graful de la b)
eulerTour = []
viz = [0 for i in range(n)]
def DFS_eulerTour(vf):
    viz[vf] = 1
    # print(vf, end = " ")
    eulerTour.append(vf)
    
    for nod in adj[vf]:
        if viz[nod] == 0:
            DFS_eulerTour(nod)
            # print(vf, end = " ")
            eulerTour.append(vf)
        
# DFS_eulerTour(0)
# print(eulerTour)



def doubleTree():

    # a) determin arborele de cost minim cu KRUSKAL - graf orientat (subpunctul b)
    kruskal()

    # c) parcurgere in adancime  => vectorul eulerTour
    DFS_eulerTour(0)
    
    s = 0
    # d) elimin duplicatele
    # print(eulerTour[0], end = " ")
    for index in range(1, len(eulerTour)):
        if eulerTour[index] not in eulerTour[:index]:
            # print(eulerTour[index], end = " ")
            
            # e) lista ramasa reprezinta solutia aproximativa
            for nod, d in la[eulerTour[index - 1]]:
                if nod == eulerTour[index]:
                    s += d
                    break
            
    print(round(s,3))
            
            

doubleTree()