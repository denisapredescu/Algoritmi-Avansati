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
print()


# 2) distanta euclidiana
def distanta_euclidiana(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3)


d = distanta_euclidiana(puncte[0], puncte[1])
print(d)   
print()


# 3) se creeaza graful complet => matrice de adiacenta; nodurile incep de la 0
def complet(n, puncte):
    
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        muchii = []
        for j in range(n): 
            if j != i:
                mat[i][j] = distanta_euclidiana(puncte[i], puncte[j])
                mat[j][i] = distanta_euclidiana(puncte[i], puncte[j])
                
    return mat


mat = complet(n, puncte)

for i in mat:
    print(i)
print()

# 4)    
solutie = [None for i in range(n)]
cmin = float('inf')

 
# Function to find the minimum weight
# Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):
    
    global cmin
 
    if (count == n and graph[currPos][0]):
        if cmin > cost + graph[currPos][0]:
            cmin = cost + graph[currPos][0]
        
        # print("************")
        # print(currPos, cost,  graph[currPos][0])
        # print("------------------")
        # for i in graph:
        #     print(i)
        return
 
    # BACKTRACKING STEP
    # Loop to traverse the adjacency list of currPos node and increasing the count
    # by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
             
            # Mark as visited
            v[i] = True
            solutie[count] = i
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])
             
            # Mark ith node as unvisited
            v[i] = False
 

v = [False for i in range(n)]
v[0] = True

# Solution array
solutie[0] = 0

tsp(mat, v, 0, n, 1, 0)

print(cmin)
print()

# 5)
solutie = [0 for i in range(n)]
viz = [0 for i in range(n)]
cmin = 0

def distanta_minima(a, l, r):
    
    global cmin
    
    if l==r:
        print(a)
        cmin = round(cmin + mat[a[0]][a[len(a)-1]], 3)      
    else:
        minim = float('inf')
        
        for nod in range(n):  
            if mat[a[l]][nod] < minim and viz[nod] == 0:
                minim = mat[a[l]][nod]
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
    
    for i in range(n):
        for j in range(n):
            if i != j:
                f.write(f"{i} {j} {mat[i][j]}\n")

    f.close()


constructieRetea("kruskal.in")    
n,m,lm = citire("kruskal.in")
    
tata=[0 for i in range(n+1)]
h=[0 for i in range(n+1)]


# b) am creat la a) arborele de cost minim cu Kruskal => se gaseste in lista de adiacenta adj graful orientat
# for u,v in muchii_pastrate:
#     creare_arb(u,v)
    
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


print("----------------------------------------------------------")
##################################################################################################################


def doubleTree():

    # a) determin arborele de cost minim cu KRUSKAL - graf orientat (subpunctul b)
    kruskal()
    
    # c) parcurgere in adancime  => vectorul eulerTour
    DFS_eulerTour(0)
    
    print(eulerTour)
    s = 0
    
    # d) elimin duplicatele
    faraD = [eulerTour[0]]
    for index in range(1, len(eulerTour)):
        if eulerTour[index] not in eulerTour[:index]:
            
            # e) lista ramasa reprezinta solutia aproximativa
            s += mat[eulerTour[index]][faraD[len(faraD) - 1]]
            faraD.append(eulerTour[index])
    

    s += mat[faraD[-1]][faraD[0]] 
    print()        
    print(round(s,3))
    
            
doubleTree()