# a)

# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity K
  
#matrice cu (n+1) linii si (K+1) coloane

# timp : O(len(S)*K)
# spatiu : O(len(S)*K)
  
def knapSack(K, S):
    n = len(S)
    M = [[0 for x in range(K + 1)] for x in range(n + 1)]
  
    # Construiec o Matrice M in care retin sumele intermediare, pas cu pas pentru greutati de la 1...K
    for i in range(n + 1):
        for k in range(K + 1):
            
            # pune 0 pe margine
            if i == 0 or k == 0:
                M[i][k] = 0
            # matricea determina de fapt suma maxima stiind ca am doar i elemente din S si capacitatea k (k = 1 ...K)
            elif S[i-1] <= k:
                M[i][k] = max(S[i-1]
                          + M[i-1][k-S[i-1]],  
                              M[i-1][k])
            else:
                M[i][k] = M[i-1][k]
  
  
    for m in M:
        print(m)
    print("--------------------------------------------")
    return M[n][K]
  
  
S = [1,3,5]  #[3, 4, 3]
K = 6
print(knapSack(K, S))

# b)
# pun in suma orice greutate care incape in suma; algoritmul nu este optim dar avand in vedere ca se 
# doreste o complexitate de spatiu de O(1), inseamna ca nu mi se permite retinerea greutatilor cu scopul de 
# a le sorta.
# Complexitatea de timp peste de O(n) pentru ca parcurg greutatile date de la tastatura

def sumab():
    
    K = int(input("Numar: "))
    suma = 0
    for nr in input("Sir numere: ").split():
        if int(nr) + suma <= K:
            suma += int(nr)
        elif suma < int(nr):
            suma = int(nr)
            
    return suma
    
print(sumab())