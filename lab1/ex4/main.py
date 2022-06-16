def citire(fisier):
    f = open(fisier)
    cuv1 = f.readline().rstrip('\n')
    cuv2 = f.readline().rstrip('\n')
    
    f.close()
    return cuv1, cuv2


# timp O(n* m)
# spatiu O(n + m + m + 4) ~ O(n + 2m) ~ O(n + m)
# n = len(cuv1)
# m = len(cuv2)
# in cel mai nefavorabil caz niciun caracter din cuv1 nu se gaseste in cuv2 si atunci 
# j va face mereu m pasi => n * m pasi in total

def celMaiLungSubsirComun(cuv1, cuv2):
    string = ""
    i = 0
    position = 0

    while i < len(cuv1):
        
        ok = 0
        j = position
        while j < len(cuv2) and ok == 0:   # cat timp inca nu s-a gasit caracterul cuv1[i], il caut in continuare in cuv2 
            if cuv1[i] == cuv2[j]:
                string += cuv1[i]
                position = j + 1
                ok = 1
            j += 1
        
        i += 1
    
    return string

cuv1, cuv2 = citire("data.in")

string = celMaiLungSubsirComun(cuv1, cuv2)
print(string)

# 2
# se face doar o verificare => O(1)
def lung1(cuv1, cuv2):
    if cuv1 == cuv2:
        print(cuv1)
        
lung1("1", "1")


# 3
# caut caracterul din primul sir in al doilea sir => maxim O(n) 
def lungN(cuv1, cuv2):
    if cuv1 in cuv2:
        print(cuv1)
    
lungN('1', "hhei12")


# 4
# timp: O(n*m)
# spatiu: O(n*m)
def distanta_de_editare(cuv1, cuv2):  # Programare dinamica
    
    c = [[0 for j in range(len(cuv1)+1)] for i in range(len(cuv2)+1)]
    
    for i in range(1, len(cuv1)+1):
        c[0][i] = 0
    for i in range(1, len(cuv2)+1):
        c[i][0] = 0

    for i in range(1, len(cuv2)+1):
        ok = 0
        for j in range(1, len(cuv1)+1):
            
            if cuv1[j-1] == cuv2[i-1] and ok == 0:
                c[i][j] = 1 + c[i-1][j-1]  
                # print(cuv1[j-1], end = '')
                ok = 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])  
                

    return c #[len(cuv2)][len(cuv1)]  

c = distanta_de_editare(cuv1, cuv2)

# print()
# for i in c:
#     print(i)

j = len(cuv1) 
i = len(cuv2)
newcuv = ""


while c[i][j] != 0:
    # print(i,j)
    if 1 + c[i-1][j-1] == c[i][j]:
        # print(cuv2[i])
        newcuv += cuv2[i]
        i -= 1
        j -= 1
    elif c[i][j-1] > c[i-1][j]:
        j -= 1
    else:
        i -= 1
newcuv += cuv2[i]   
print(newcuv[::-1])      
            
