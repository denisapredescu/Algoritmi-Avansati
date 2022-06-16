from scipy.optimize import linprog

##### LAB 4 / ex 1

# max 180x + 200y   => min  - 180x - 200y
#  5x + 4y ≤ 80
#10x + 20y ≤ 200
#        x ≥ 0
#        y ≥ 0

obj = [-180, -200]

lhs_ineq = [[5, 4], 
            [10, 20]] 

rhs_ineq = [ 80, 
            200] 

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
print(opt)

# con: array([], dtype=float64)
#      fun: -3066.6666666666665
#  message: 'Optimization terminated successfully.'
#      nit: 2
#    slack: array([0., 0.])
#   status: 0
#  success: True
#        x: array([13.33333333,  3.33333333]) 

print(f"x = {opt.x[0]}, y = {opt.x[1]} => profitul maxim: {abs(opt.fun)}")