import math

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
        
        
        
c = cromozon(2, 4, 8)  # a b n
c.setSir([0,0,0,1,1,1,1,1])  # nr = 31
print(c.sirInNumar())

print()

c = cromozon(1, 2, 4)  # a b n
c.setSir([1,1,1,1,1,1,0,1])   # nr = 13; self.sir = [1,1,0,1]
print(c.sirInNumar())

print()

c = cromozon(-1, 4, 8)  # a b n
c.setSir([0,0,0,1,1,0,0,1])  # nr = 25
print(c.sirInNumar())    # -0.51171875

print()

c = cromozon(-1, 4, 6)  # a b n
c.setSir([0,0,0,1,1,0,0,1])  # nr = 25
print(c.sirInNumar())     # 0.953125


