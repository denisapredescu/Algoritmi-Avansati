# a, b = [int(x) for x in input().split()]
# n = int(input())
# interv = []
# for i in range(n):
#     x, y = [int(i) for i in input().split()]
#     if not(y <= a or x >= b):
#         interv.append([x, y])

# interv.sort(key=lambda x : (x[0], -x[1])) # cresc dupa primul elem, descresc dupa ult elem
# print(interv)

# alese = []
# ok = 1

# if interv[0][0] > a: # nu exista interval care sa il cuprinda pe a
#     ok = 0
# else:
#     i = 0
#     while i < len(interv) and ok == 1:
#         x, y = interv[i - 1]
        
#         while interv[i][0] == x and i < len(interv):
#             i += 1

#         if len(alese) >= 2:  # tai din alese intervalele ce sunt cuprinse in alte reuniuni de intervale
#             while alese[len(alese)-2][1] >= interv[i][0] and len(alese) >= 2:
#                 alese = alese[:len(alese)-1]
#         alese.append(interv[i])
#         j = len(alese) - 1
    
#         while interv[i][1] <= alese[j][1] and i < len(interv):
#             i += 1
            
#         if alese[j][1] >= b:
#             ok = 0
        
# if len(alese) != 0:
#     print(alese)
# else:
#     print("nu se poate")


a, b = [int(x) for x in input().split()]
n = int(input())
interv = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    if not(y <= a or x >= b):
        interv.append([x, y])

interv.sort(key=lambda x : x[0]) # cresc dupa primul elem, descresc dupa ult elem

alese = []
ok = 0

# vreau intervalele ce se termina cel mai departe de a si il contin pe a

if interv[0][0] > a: # nu exista interval care sa il cuprinda pe a
    print("Nu se poate")
else:
    i = 0
    x = 0 
    y = 0
    while i < len(interv) and ok == 0:
        while i < len(interv) and interv[i][0] <= a:
            if y < interv[i][1]:
                x = interv[i][0]
                y = interv[i][1]
            i += 1
        
        alese.append([x, y])
        a = y # resetez a -ul => noua mea tinta
        
        if y >= b:
            ok = 1
        
if ok != 0:
    print(alese)
else:
    print("Nu se poate")