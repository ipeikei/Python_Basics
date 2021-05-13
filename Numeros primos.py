lista = 100
cont = 0
for i in range(2, lista + 1):
    primos = True
    for j in range(2,11):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
