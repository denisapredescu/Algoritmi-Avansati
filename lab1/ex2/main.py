import heapq

class BinaryTreeNode:
    def __init__(self, number, car = None):
        self.number = number
        self.character = car
        self.leftChild = None
        self.rightChild = None
        
    def __lt__(self, otherNode):  # overloading operator <
        if(self.number < otherNode.number):
            return True
        return False


# pentru a retine numarul de aparitie a fiecarui caracter, construiect un vector de frecventa
# dictionar in care cheia este caracterul si valoarea este numarul de aparitie a acestuia.

# citirea se face in O(n) unde n reprezinta numarul de caractere din fisier
# citesc din fisier textul
def citire(fisier):
    f = open(fisier)
    cuv = f.read()
    f.close()
    return cuv


# subpunctul 1)
# functia returneaza pentru fiecare caracter gasit numarul de aparitie a acestuia
# timp: O(n) - parcurg textul
# spatiu: O(n): textul ocupa n spatii, dictionarul ocupa sigur mai putin de n => O(2n) => O(n)
def vectorFrecv(text): 
    d = {}
    for lit in text:
        d[lit] = d.get(lit, 0) + 1 
    
    return d   #returnez dictionarul


########################### subpunctul 2)

# fiecare litera va deveni un nod din arbore in care in variabila "number" retin numarul
# de aparitii si in "character" litera corespunzatoare. Avand in vedere ca literele vor 
# fi frunze, leftChild si rightChild nu vor pointa spre niciun alt nod. 

# am nevoie de un heap pentru ca algoritmul lui Huffman ia literele sortate in ordine crescatoare
# a numarul lor de aparitii  => O(n log n)
# spatiu O(n); unde n - fiecare caracter diferit

def creareHeap(frecv):
   
    h = []
    for key in frecv.keys(): 
        node = BinaryTreeNode(frecv[key], key)
        heapq.heappush(h, node)
    return h  


# algoritmul lui Huffman se opreste cand se ajunge la un arbore cu radacina
# la fiecare pas din primii 2 arbori cu cantitate minima se creeaza un singur arbore =>
# deci scoatem 2 noduri din heap si introducem unul.  => O(n log n)
# spatiu: la final vor fi n(n-1)/2 noduri => O(n^2)

def arboreHuffman(frecv):

    h = creareHeap(frecv)   # apelez functia creareHeap prin care se creaza heapul cu structurile create
    while len(h) != 1:
        
        x = heapq.heappop(h)   # extrag primele 2 structuri cu variabila "number" minima
        y = heapq.heappop(h)

        rad = BinaryTreeNode(x.number + y.number)     # creez structura suma si o adaug in heap
        rad.leftChild = x
        rad.rightChild = y
        
        heapq.heappush(h, rad)
        
    # la final returnez radacina arborelui rezultat
    return rad


# subpunctul 2) codificare  -> arbore Huffman
# creez codul specific unui caracter => in functie de copilul ales leftChild, respectiv rightChild,
# se va adauga 0, respectiv 1, la finalul codului pana se ajunge la o frunza => O(n) unde n este numarul de noduri
# spatiu: am arborele cu 2*n noduri (la fiecare pas se mai adauga un nod pana cand am un arbore cu radacina) =>
# O(n); 1 string care va fi mereu modificat; un dictionar cu n pozitii => O(n)
def codificareHuffman(rad, string, codHuffman):
    
    if rad.leftChild != None:    
        string += '0'
        codificareHuffman(rad.leftChild, string, codHuffman)
        string = string[:len(string) - 1]
        
    if rad.rightChild != None:
        string += '1'
        codificareHuffman(rad.rightChild, string, codHuffman)  
        string = string[:len(string) - 1]
    
    if rad.character != None:
        codHuffman[rad.character] = string



################################# subpunctul 3)  codificare
# in locul fiecarui caracter afisez codul sau
# complexitate timp O(m) unde m = len(text)

def encodedString(text, arb):
    
    g = open("write.txt", "w")
    for i in text:
        g.write(arb[i])
    g.close()
    

################################# subpunctul 4)   decodificare

# din codurile caracterelor (dictionar) creez arborele Huffman astfel incat sa il
# pot parcurge mai usor si sa determin ordinea literelor
# timp: O(numarul de 0 si 1 din codurile caracterelor)
# spatiu creez un arbore cu rad: O(n) - n - nr de caractere diferite
def creareArbDinHuffman(huffman):
    
    rad = BinaryTreeNode(0)
    
    for lit in huffman.keys():
       
        x = rad    #mereu plec din radacina creata si in functie de etichete maa misc in arbore sau creez noi noduri
        for cod in huffman[lit]:
            if cod  == '0':
                if x.leftChild != None:
                    x = x.leftChild       
                else:
                    y = BinaryTreeNode(0)
                    x.leftChild = y
                    x = y     
            if cod == '1': 
                if x.rightChild != None:
                    x = x.rightChild
                else:
                    y = BinaryTreeNode(0)
                    x.rightChild = y
                    x = y
              
        # sigur am ajuns la o frunza => trebuie sa zic ce caracter are traseul parcurs      
        x.character = lit
        
    return rad   # returnez radacina: astfel pastrez arborele
        
        
# dupa ce am creat arborele Huffman, trebuie sa decodific sirul de caractere format din 0 si 1 
# timp: O(lungimea sirului = m)
# 
def decoded(rad, sir):      
    
    # ok poate avea 2 valori
    # 0 daca totul este ok (nu am ajuns la finalul sirului)
    # 1 daca am ajuns la finalul sirului

    ok = 0
    if len(sir) == 0:     # daca nu exista sir de caractere, nu se va intampla nimic
            ok = 2
    nod = rad  # incep de la radacina sa ma plimb in jos in arbore in functie de ordinea din sir
        
    while ok == 0:  # cat timp nu s-a terminat sirul
        if sir[0] == '0':   # ma duc pe stanga
            if nod.leftChild != None: 
                nod = nod.leftChild
                sir = sir[1:]
                
                if len(sir) == 0:  # mereu verific daca am ajuns la final => daca nu fac asta, la urmatoarea bucla a whileului va face text[0] eroare
                    ok = 2
                    print(nod.character, end='')   # am ajuns la final, deci sigur sunt pe o frunza    
            else:
                # urmatorul caracter din sir e 0 si nu am fiu stang inseamna ca sunt pe o frunza
                print(nod.character, end='')
                nod = rad    # ma intorc la radacina si incep din nou parcurgerea pana la o frunza
                
        elif sir[0] == '1':
            if nod.rightChild != None:
                nod = nod.rightChild
                sir = sir[1:]
                
                if len(sir) == 0:
                    ok = 2
                    print(nod.character, end='')     
            else:
                print(nod.character, end='')  # am ajuns la final, deci sigur sunt pe o frunza
                nod = rad
                

# subprogramul doar uneste functiile definite anterior
# adica transforma codul Huffman intr-un arbore cu radacina
# si apoi decodifica textul
# O(lungimea sirului + nr de 0 si 1 din codurile tuturor caracterelor)
def decodedString(sir, arb):
    rad = creareArbDinHuffman(arb)
    decoded(rad, sir)


################################# subpunctul 5) 
# textul cu operele lui Shakespeare se gaseste in fisierul "ex15.in"

def compresie(fisier):
    
    text = citire(fisier)   # citesc textul
    frecv = vectorFrecv(text)  # determin vectorul de frecventa = dictionar
    
    rad = arboreHuffman(frecv)   # determin arborele huffman
    
    codHuffman = {}
    codificareHuffman(rad, '', codHuffman)  # determin codurile huffman corespunzatoare caracterelor din text
    
    encodedString(text, codHuffman)  # encodez textul
    
    
    
# 1)   
text = citire("ex2.in")
frecv = vectorFrecv(text)
print(frecv)
# scriereFrecv()

# 2)
radacina = arboreHuffman(frecv)
codHuffman = {}
codificareHuffman(radacina, '', codHuffman)
print(codHuffman)

# 3 si 5 se scriu in acelasi fisier de iesire 
# 3)
encodedString("Huffman coding is a data compression algorithm.", {'l': '00000', 'p': '00001', 't': '0001', 'h': '00100', 'e': '00101', 'g': '0011', 'a': '010', 'm': '0110', '.': '01110', 'r': '01111', ' ': '100', 'n': '1010', 's': '1011', 'c': '11000', 'f': '11001', 'i': '1101', 'o': '1110', 'd': '11110', 'u': '111110', 'H': '111111'})


# 4)
decodedString("11111111111011001110010110010101010011000111011110110110100011100110110111000101001111001000010101001100011100110000010111100101101110111101111010101000100000000111110011111101000100100011001110", {'l': '00000', 'p': '00001', 't': '0001', 'h': '00100', 'e': '00101', 'g': '0011', 'a': '010', 'm': '0110', '.': '01110', 'r': '01111', ' ': '100', 'n': '1010', 's': '1011', 'c': '11000', 'f': '11001', 'i': '1101', 'o': '1110', 'd': '11110', 'u': '111110', 'H': '111111'})

# 5)
compresie("ex25.in")

    

