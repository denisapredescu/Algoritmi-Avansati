import random
import math


fisier = open("Evolutie.txt", "w")

class cromozon:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.sir = [False for x in range(n)]
        self.p = (b - a) / math.pow(2,n)
    
    def sirInNumar(self):
        # a)
        nr = 0
        for i in range(self.n):
            nr += math.pow(2, i) * self.sir[-1 - i]
        # b)
        inm = nr * self.p
        # c)
        ad = inm + self.a
        
        return ad
    
    def setSir(self, s):
        if len(self.sir) == len(s):
            self.sir = s
        else:
            m = len(s)
            n = self.n
            while m != 0 and n != 0:
                self.sir[n-1] = s[m-1]
                m -= 1
                n -= 1
        

def citire(fisier):
    f = open(fisier)
    dim_pop = int(f.readline())
    dom_def = [int(x) for x in f.readline().split()]
    param = [int(x) for x in f.readline().split()]
    precizie = int(f.readline())
    prob_recombinare = float(f.readline())
    prob_mutatie = float(f.readline())
    nr_etape = int(f.readline())
    
    return dim_pop, dom_def, param, precizie, prob_recombinare, prob_mutatie, nr_etape

dim_pop, dom_def, param, precizie, prob_recombinare, prob_mutatie, nr_etape = citire("lab3.in")
print(dim_pop, dom_def, param, precizie, prob_recombinare, prob_mutatie, nr_etape)


# 1
lista_crom = [[]]   # cromozomii incep de pe poz 1. De ce?  cromozonul 1 se afla in intervalul [q0, q1)
for i in range(dim_pop):
    lista_crom.append(random.choices([0,1], k=22))
 
 

def f(x):
    rez = 0
    put = 1  # x^0
    for p in param[::-1]:
        rez += p * put 
        put *= x
         
    return rez

crom = cromozon(dom_def[0], dom_def[1], len(lista_crom[1]))  # folosesc acelasi variabila - structura - cromozon => ii schimb doar valoarea din cromozonului

def x_fx():
    # creez listele x si fx pentru a le afisa in fisier
    
    x, fx = [0], [0]
    for i in range(1, dim_pop + 1):
        crom.setSir(lista_crom[i])
        x.append(crom.sirInNumar())
        fx.append(f(x[i]))
        
    return x, fx
    

# afisez in fisier Cromozon x fx
def afisare_Cromozon_x_fx(mesaj):

    fisier.write(f"{mesaj}\n")
    for i in range(1, dim_pop + 1):
        fisier.write(f'{str(i):3s}: {"".join(map(str,lista_crom[i]))} ')
        fisier.write(f'x = {str(round(x[i], 6)):9} f = {fx[i]} \n')



x, fx = x_fx()
# afisez in fisier populatia initiala #####################################
afisare_Cromozon_x_fx("Populatia initiala")
###########################################################################


# 2
s = sum(fx)  

pi = [0]     # incep de la 1. De ce? qi = p1 +....+pi;   cromozonul 1 se afla in intervalul [q0, q1) 
for i in range(1, dim_pop + 1):
    pi.append(fx[i]/s)
    
    
# afisez in fisier probabilitatile de selectie (subpunctul 2) #################
fisier.write("\nProbabilitati selectie\n")
for i in range(1, dim_pop + 1):
    fisier.write(f'cromozon   {str(i):3s} probabilitate  {pi[i]} \n')
###############################################################################

    
# 3
q = []
s = 0
for i in pi:
    s += i
    q.append(s)

# afisez in fisier intervalele probabilitati selectie ########################
fisier.write("Intervale probabilitati selectie\n")
for i in range(dim_pop + 1):
    fisier.write(f'{q[i]}  ')
    if (i+1) % 4 == 0:
        fisier.write('\n')
##############################################################################


# 4 cautare binara : selectarea cromozonului dorit; n cromozoni

for i in range(dim_pop + 1):   
    print(i, lista_crom[i], q[i])


def cautareBinara(b, e, x):
    i = int((b + e) /2)
    if x >= q[i] and x < q[i+1]:
        return i+1
    
    if x < q[i]:
        return cautareBinara(b, i, x)
    else: 
        return cautareBinara(i+1, e, x) 
    
     
def selectie(n):
    
    nr_cromozoni = []
    cromozoni = [[]]
    
    fisier.write("\n")
    
    while n != 0:
        value = random.random()
        nr_crom = cautareBinara(0, len(lista_crom)-1, value)

        nr_cromozoni.append(nr_crom)
        cromozoni.append(lista_crom[nr_crom])
        
        fisier.write(f'u = {value}   selectam cromozonul  {nr_crom} \n')
        
        n -= 1
    
    return cromozoni, nr_cromozoni
    

lista_crom, nr_cromozoni = selectie(dim_pop)   # lista cu cromozoni incepe de la 0 
# x si fx sunt listele facute anterior, ele sunt numerotate de la 1 => nu este nevoie sa scad 1 

# 5 
# afisarea cromozonilor care participa la recombinare ########################
fisier.write("Dupa selectie:\n")
for i in range(1, dim_pop + 1):
    fisier.write(f'{str(i):3s}: {"".join(map(str,lista_crom[i]))} ')
    fisier.write(f'x = {str(round(x[nr_cromozoni[i - 1]], 6)):9} f = {fx[nr_cromozoni[i - 1]]} \n')

##############################################################################

# nu vom mai avea nevoie de afisari la subpunctul 9
# pe noua lista de cromozoni
fisier.write(f"\nProbabilitatea de incrucisare {prob_recombinare}\n")
# indici = [] # indicii cromozonilor care vor parcicipa la incrucisare
def indici_probabililitate_incrucisare(af_mesaj = False, indici = []):
    for i in range(1, dim_pop + 1):
        
        value = random.random()
        
        if af_mesaj == True:
            fisier.write(f'{str(i):3s}: {"".join(map(str,lista_crom[i]))} ')
            fisier.write(f'u = {str(value)}')
        
        if value < prob_recombinare:
            
            if af_mesaj == True:
                fisier.write(f' < {prob_recombinare} participa')
                
            indici.append(i)
        
        if af_mesaj == True:
            fisier.write('\n')
    
    if af_mesaj == True:   
        fisier.write('\n')
        
    return indici
indici = indici_probabililitate_incrucisare(True)

# 6
def recombanare(lista_crom, af_mesaj = False):
    while len(indici) > 1:
        x = random.choice(indici)
        indici.remove(x)
        y = random.choice(indici)
        indici.remove(y)
        
        crom_x = lista_crom[x]
        crom_y = lista_crom[y]
        
        punct = random.randint(0, 21)
        
        if af_mesaj == True:
            fisier.write(f'Recombinare dintre cromozonul {x} cu cromozonul {y}:\n')
            fisier.write(f'{"".join(map(str,crom_x))} {"".join(map(str,crom_y))} punct {punct} \n')
        
        # print(crom_x)
        # print(crom_y)
        
        aux = crom_x[:punct]
        crom_x = crom_y[:punct] + crom_x[punct:]
        crom_y = aux + crom_y[punct:]
        
        # print(punct)
        # print(crom_x)
        # print(crom_y)
        
        if af_mesaj == True:
            fisier.write(f'Rezultat {"".join(map(str,crom_x))} {"".join(map(str,crom_y))}\n')
            
        lista_crom[x] = crom_x
        lista_crom[y] = crom_y
        
    return lista_crom


# pentru 6 este nevoie sa creez recombinari si sa ajusez mesajele => acelasi cod se va folosi si pentru 9 (fara mesaje)

lista_crom = recombanare(lista_crom, True)
            
# 7 => acelasi cod ca la 1

# x = [0]
# fx = [0]

# creez listele x si fx pentru a le afisa in fisier
x, fx= x_fx()


# for i in range(1, dim_pop + 1):
#     crom.setSir(lista_crom[i])
#     x.append(crom.sirInNumar())
#     fx.append(f(x[i]))
    
# afisez in fisier populaţia rezultată după recombinare ####################
# fisier.write("Dupa recombinare:\n")
# for i in range(1, dim_pop + 1):
#     fisier.write(f'{str(i):3s}: {"".join(map(str,lista_crom[i]))} ')
#     fisier.write(f'x = {str(round(x[i], 6)):9} f = {fx[i]} \n')

afisare_Cromozon_x_fx("Dupa recombinare")
############################################################################


# 8

fisier.write(f"\nProbabilitate de mutatie pentru fiecare gena {prob_mutatie}\n")
fisier.write(f"Au fost modificati cromozomii:\n")
# din exemplul din fisier am inteles ca este folosita varianta 1 din curs (adica pentru un cromozon se modifica cel mult o gena)
# dar pentru ca probabilitatea este foarte mica, folosesc varianta 2
def mutatie(lista_crom, af_mesaj = False):
    for i in range(1, dim_pop + 1):    
        ok = 0
        for j in range(len(lista_crom[i])):   
            value = random.random()

            if value < prob_mutatie:
                if ok == 0:
                    if af_mesaj == True:
                        fisier.write(f"{str(i)}\n")
                    ok = 1 # ca sa apara doar o data ca modificat
                
                lista_crom[i][j] = (lista_crom[i][j] + 1) % 2
                
    return lista_crom


lista_crom = mutatie(lista_crom, True)


# acelasi cod ca la 1

# x = [0]
# fx = [0]

# creez listele x si fx pentru a le afisa in fisier
# for i in range(1, dim_pop + 1):
#     crom.setSir(lista_crom[i])
#     x.append(crom.sirInNumar())
#     fx.append(f(x[i]))

x, fx = x_fx()
    
# afisez in fisier populaţia rezultată după recombinare ####################
# fisier.write("Dupa mutatie:\n")
# for i in range(1, dim_pop + 1):
#     fisier.write(f'{str(i):3s}: {"".join(map(str,lista_crom[i]))} ')
#     fisier.write(f'x = {str(round(x[i], 6)):9} f = {fx[i]} \n')
afisare_Cromozon_x_fx("Dupa mutatie:")
############################################################################       

# 9
fisier.write("\nEvolutia maximului\n")
for i in range(nr_etape):
    
    indici = indici_probabililitate_incrucisare()
    lista_crom = recombanare(lista_crom)
    lista_crom = mutatie(lista_crom)

    x, fx = x_fx()
    
    maxim = max(fx)
    fisier.write(f"{maxim}\n")
     

fisier.close()