n = 20

# 1
# timp O(2^n)
# spatiu O(n) => 
# => As you can see the maximum depth is proportional to the N, hence the space complexity of Fibonacci 
# recursive is O(N)

def fibonacciRecursiv(n):
    
    if n <= 1:
        return 1

    n1 = fibonacciRecursiv(n-1)
    n2 = fibonacciRecursiv(n-2)
    return n1 + n2

print(fibonacciRecursiv(n))


# 2
# timp: O(n) => oricare ar fi n >= 2, algoritmul va lua valorile de pe ultimel 2 pozitii dinaintea lui n; am n numere => O(n)
# spatiu: O(n) => am vectorul in care introduc primii n termeni ai sirului lui Fibonacci

def fibonacciVector(n):
    
    if n <= 1:
        v[n] = 1
      
    if v[n] == None:     #in cazul in care nu am inserat niciun numar pe pozitia respectiva, determin recursiv numarul
        v[n-1] = fibonacciVector(n-1)
        v[n-2] = fibonacciVector(n-2)
        v[n] = v[n-1] + v[n-2]
  
    return v[n]    # returnez numarul de pe pozitia dorita


v = [None for i in range(n+1)]
print(fibonacciVector(n))
# print(v[-1])


# 3
# timp: O(n) => am n numere de calculat
# spatiu: O(1)  => retin in variabilele x, x, z, n => O(4) ~ O(1)

def fibonacciIterativ(n):
    
    x = 1 
    y = 1
    while n != 1:
        z = x + y
        x = y
        y = z
        n -= 1
    
    return z
        
print(fibonacciIterativ(n))
        