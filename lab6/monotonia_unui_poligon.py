# algoritmul nu este eficient; varianta optima este monotonie2.py
def determinant( x1, y1, x2, y2, x3, y3):
    return x2 * y3 + x1 * y2 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

n = int(input())

p = []
index = 0
for i in range(n):
    xy = [int(x) for x in input().split()]
    p.append([index, xy[0], xy[1]])
    index += 1
  

def monotonie(sorted_p, viz = [0] * n, stack = []):
    
    stack.append(p[0])
    viz[p[0][0]] = 1
    stack.append(p[1])
    viz[p[1][0]] = 1
    
    for i in range(2,n):
            
        if sorted_p[i][0] == (sorted_p[i-1][0] + 1) % n or sorted_p[i][0] == (sorted_p[i-1][0] - 1) % n:  # caz 2
            
            if determinant(sorted_p[i-2][0], sorted_p[i-2][1], sorted_p[i-1][0], sorted_p[i-1][1], sorted_p[i][0], sorted_p[i][1]) > 0: # viraj la stanga
                # caz 2b
                stack.append(sorted_p[i])
                viz[sorted_p[i][0]] = 1
            else:
                # caz 2a
                j = i
                while j >= 2 and determinant(sorted_p[j-2][0], sorted_p[j-2][1], sorted_p[j-1][0], sorted_p[j-1][1], sorted_p[j][0], sorted_p[j][1]) < 0 and len(stack) > 0:
                    stack.pop()
                    viz[sorted_p[j][0]] = 0
                    
                stack.append(sorted_p[i])
                viz[sorted_p[i][0]] = 1
                    
        else: # nu se afla pe acelasi lant => caz 1
            pct_pastrat = stack.pop()
            viz[pct_pastrat[0]] = 0
            if viz[(sorted_p[i][0] - 1) % n] == 0 and viz[(sorted_p[i][0] + 1) % n] == 0:  # nu are legatura cu niciun alt nod determinat
                return "NO"
            
            if  len(stack) > 0: # am mai sus legatura, tai varfurile pana la acela inclusiv
                
                pct = stack.pop()
                viz[pct[0]] = 0
                while (pct[0] == (sorted_p[i][0] - 1) % n or pct[0] == (sorted_p[i][0] + 1) % n)  and len(stack) > 0:
                    pct = stack.pop()
                    viz[pct[0]] = 0
                
                # if (viz[(sorted_p[i][0] - 1) % n] == 1 or viz[(sorted_p[i][0] + 1) % n] == 1) and len(stack) > 0:
                #     pct = stack.pop()
                #     viz[pct[0]] = 0
                #     while (pct[0] == (sorted_p[i][0] - 1) % n or pct[0] == (sorted_p[i][0] + 1) % n)  and len(stack) > 0:
                #         pct = stack.pop()
                #         viz[pct[0]] = 0
                
                
            stack.append(pct_pastrat)
            viz[pct_pastrat[0]] = 1
            stack.append(sorted_p[i]) 
            viz[sorted_p[i][0]] = 1
    
        
    if len(stack) <= 2:
        return "YES"
    else:
        return "NO"




# x - monotomia
# sortez punctele dupa x
sorted_x = p
sorted_x.sort(key=lambda x:(x[1]), reverse=False)

print(monotonie(sorted_x))



# y - monotomia
# sortez punctele dupa y
sorted_y = p
sorted_y.sort(key=lambda x:(x[2]), reverse=True)
print(monotonie(sorted_y))
















# ########################################################################3
# # y - monotomia
# # sortez punctele dupa y
# sorted_y = p
# sorted_y.sort(key=lambda x:(x[2]), reverse=True)
# viz = [0] * n

# print(sorted_y)
# stack = [] # stiva pentru varfuri

# for i in range(n):
#     if i <= 0:
#         stack.append(p[i])
#         viz[p[i][0]] = 1
    
#     else:
#         print(sorted_y[i])
#         if sorted_y[i][0] == (sorted_y[i-1][0] + 1) % n or sorted_y[i][0] == (sorted_y[i-1][0] - 1) % n:  # caz 2
#             print("caz 2")
#             if determinant(sorted_y[i-2][0], sorted_y[i-2][1], sorted_y[i-1][0], sorted_y[i-1][1], sorted_y[i][0], sorted_y[i][1]) > 0: # viraj la stanga
#                 # caz 2b
#                 print("b")
#                 stack.append(sorted_y[i])
#                 viz[sorted_y[i][0]] = 1
#             else:
#                 print("a")
#                     # caz 2a
#                 j = i
#                 while j >= 2 and determinant(sorted_y[j-2][0], sorted_y[j-2][1], sorted_y[j-1][0], sorted_y[j-1][1], sorted_y[j][0], sorted_y[j][1]) < 0 and len(stack) > 0:
#                     stack.pop()
#                     viz[sorted_y[j][0]] = 0
#                 stack.append(sorted_y[i])
#                 viz[sorted_y[i][0]] = 1
                    
#         else: # nu se afla pe acelasi lant => caz 1
#             print("caz 1")
#             pct_pastrat = stack.pop()
#             viz[pct_pastrat[0]] = 0
            
#             print(viz[(sorted_y[i][0] - 1) % n], viz[(sorted_y[i][0] + 1) % n]) 
#             if (viz[(sorted_y[i][0] - 1) % n] == 1 or viz[(sorted_y[i][0] + 1) % n] == 1) and len(stack) > 0: # am mai sus legatura, tai varfurile pana la acela inclusiv
                
#                 pct = stack.pop()
#                 viz[pct[0]] = 0
#                 print("renunt la ", pct)
#                 print("stack ramas", stack)
#                 while (pct[0] == (sorted_y[i][0] - 1) % n or pct[0] == (sorted_y[i][0] + 1) % n)  and len(stack) > 0:
#                     pct = stack.pop()
#                     viz[pct[0]] = 0
#                     print("renunt la ", pct)
#                     print("stack ramas", stack)
                
#                 print(viz[(sorted_y[i][0] - 1) % n], viz[(sorted_y[i][0] + 1) % n]) 
#                 if (viz[(sorted_y[i][0] - 1) % n] == 1 or viz[(sorted_y[i][0] + 1) % n] == 1) and len(stack) > 0:
#                     pct = stack.pop()
#                     viz[pct[0]] = 0
#                     print("renunt la ", pct)
#                     print("stack ramas", stack)
#                     while (pct[0] == (sorted_y[i][0] - 1) % n or pct[0] == (sorted_y[i][0] + 1) % n)  and len(stack) > 0:
#                         pct = stack.pop()
#                         viz[pct[0]] = 0
#                         print("renunt la ", pct)
#                         print("stack ramas", stack)
                
#                 # if pct == pct_pastrat:
                
#             stack.append(pct_pastrat)
#             viz[pct_pastrat[0]] = 1
#             stack.append(sorted_y[i]) 
#             viz[sorted_y[i][0]] = 1
#     print(stack)
                
# if len(stack) <= 2:
#     print("YES")
# else:
#     print("NO")
                


        
