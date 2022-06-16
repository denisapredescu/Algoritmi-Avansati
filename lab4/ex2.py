### LAB 4 / ex 2

from scipy.optimize import linprog

# (x1 ∨ x2 ∨ x4) ∧ (x1 ∨ x3 ∨ x5) ∧ (x2 ∨ x4 ∨ x5)
# Programul liniar corespunzător ar fi:
# min x1 + x2 + x3 + x4 + x5
#   x1 + x2 + x4 ≥ 1
#   x1 + x3 + x5 ≥ 1
#   x2 + x4 + x5 ≥ 1
    # 0 ≤ x1 ≤ 1
    # 0 ≤ x2 ≤ 1
    # 0 ≤ x3 ≤ 1
    # 0 ≤ x4 ≤ 1
    # 0 ≤ x5 ≤ 1

file = open("file_ex2.txt")

obj = []
lhs_ineq = []
rhs_ineq = []
minim = set()
C = []

for line in file.readlines():
    c = []
    for elem  in line.split():
        minim.add(int(elem[1:]))
        c.append(int(elem[1:]))
        
    C.append(c)
        
file.close()

nr_elem = len(minim)

for linie in C:
    line_lhs = []
    for nr in range(1, nr_elem + 1):
        if nr in linie:
            line_lhs.append(-1)
        else:
            line_lhs.append(0)
            
    lhs_ineq.append(line_lhs)
                 
for i in range(len(C)):
    rhs_ineq.append(-1)  

for i in range(len(minim)):
    obj.append(1)


opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
print(opt)

#  con: array([], dtype=float64)
#      fun: 1.5
#  message: 'Optimization terminated successfully.'
#      nit: 3
#    slack: array([0., 0., 0.])
#   status: 0
#  success: True
#        x: array([0.5, 0.5, 0. , 0. , 0.5])

xi = []

for elem in opt.x:
    if elem >= 1/3:
        xi.append(True)
    else:
        xi.append(False)
        
print(f"Solutie: {xi}")  # [True, True, False, False, True]