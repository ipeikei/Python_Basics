# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:07:24 2021

@author: vicky
"""
def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

idDuoc=input('Bienvenido al CineDuoc \nPertenece usted a Duoc UC? s/n')

if idDuoc.upper()=='S':
    Descuento=True
    while Descuento==True:
        #Entradas
        opcion=0   
        while opcion!=3:
            print('Escoja su tipo de entrada')
            print(f'1. Estreno: $4.800')
            print(f'2. Normal: $2.900')
            print(f'3. Salir')
            opcion= pedirNumeroEntero()
            totalEntradas=0
            TipoEntrada=('')        
            if opcion==1:
                totalEntrada=4800
                TipoEntrada=('Estreno')
                break
            elif opcion==2:
                totalEntrada=2900
                TipoEntrada=('Normal')
                break
            elif opcion==3:
                print('Muchas gracias por visitarnos')
                break
            else:
                print ("Introduce un numero entre 1 y 3")            
        #Palomitas
        opcion=0   
        while opcion!=4:
            print('Desea palomitas?')
            print(f'1. Pequeñas: $2.500')
            print(f'2. Medianas: $4.500')
            print(f'3. Grandes: $7.800')
            print(f'4. No gracias')
            opcion= pedirNumeroEntero()
            totalPalomitas=0
            TipoPalomitas=('')        
            if opcion==1:
                totalPalomitas=2500
                TipoPalomitas=('Pequeñas')
                break
            elif opcion==2:
                totalPalomitas=4500
                TipoPalomitas=('Medianas')   
                break
            elif opcion==3:
                totalPalomitas=7800
                TipoPalomitas=('Grandes')
                break
            elif opcion==4:
                print('Muchas gracias')
                break
            else:
                print ("Introduce un numero entre 1 y 4")                
        #Bebidas
        opcion=0   
        while opcion!=4:
               print('Desea bebida?')
               print(f'1. Pequeñas: $1.000')
               print(f'2. Medianas: $1.250')
               print(f'3. Grandes: $2.000')
               print(f'4. No gracias')
               opcion= pedirNumeroEntero()
               totalBebida=0
               TipoBebida=('')      
               if opcion==1:
                   totalBebida=1000
                   TipoBebida=('Pequeñas')
                   break
               elif opcion==2:
                   totalBebida=1250
                   TipoBebida=('Medianas')  
                   break
               elif opcion==3:
                   totalBebida=2000
                   TipoBebida=('Grandes')
                   break
               elif opcion==4:
                   print('Muchas gracias')
                   break
               else:
                   print ("Introduce un numero entre 1 y 4")        
        break
    #Total
    total=float(totalBebida+totalEntrada+totalPalomitas)
    pago=float(input(f'Su total a pagar es de {total} \nCon cuanto desea pagar?'))
    if pago>total:
             vuelto=float((pago-total)*0.70)
             print(f'Su vuelto es de ${vuelto}')
    else:
             print('Monto insuficiente.')
             
elif idDuoc.upper()=='N':
    Descuento=False
    while Descuento==False:
        total=0
        #Entradas
        opcion=0   
        while opcion!=3:
            print('Escoja su tipo de entrada')
            print(f'1. Estreno: $4.800')
            print(f'2. Normal: $2.900')
            print(f'3. Salir')
            opcion= pedirNumeroEntero()
            totalEntradas=0
            TipoEntrada=('')        
            if opcion==1:
                totalEntrada=4800
                TipoEntrada=('Estreno')
                break
            elif opcion==2:
                totalEntrada=2900
                TipoEntrada=('Normal')
                break
            elif opcion==3:
                print('Muchas gracias por visitarnos')
                break
            else:
                print ("Introduce un numero entre 1 y 3")            
        #Palomitas
        opcion=0   
        while opcion!=4:
            print('Desea palomitas?')
            print(f'1. Pequeñas: $2.500')
            print(f'2. Medianas: $4.500')
            print(f'3. Grandes: $7.800')
            print(f'4. No gracias')
            opcion= pedirNumeroEntero()
            totalPalomitas=0
            TipoPalomitas=('')        
            if opcion==1:
                totalPalomitas=2500
                TipoPalomitas=('Pequeñas')
                break
            elif opcion==2:
                totalPalomitas=4500
                TipoPalomitas=('Medianas')   
                break
            elif opcion==3:
                totalPalomitas=7800
                TipoPalomitas=('Grandes')
                break
            elif opcion==4:
                print('Muchas gracias')
                break
            else:
                print ("Introduce un numero entre 1 y 4")                
        #Bebidas
        opcion=0   
        while opcion!=4:
               print('Desea bebida?')
               print(f'1. Pequeñas: $1.000')
               print(f'2. Medianas: $1.250')
               print(f'3. Grandes: $2.000')
               print(f'4. No gracias')
               opcion= pedirNumeroEntero()
               totalBebida=0
               TipoBebida=('')      
               if opcion==1:
                   totalBebida=1000
                   TipoBebida=('Pequeñas')
                   break
               elif opcion==2:
                   totalBebida=1250
                   TipoBebida=('Medianas')  
                   break
               elif opcion==3:
                   totalBebida=2000
                   TipoBebida=('Grandes')
                   break
               elif opcion==4:
                   print('Muchas gracias')
                   break
               else:
                   print ("Introduce un numero entre 1 y 4")        
        break
    #Total
    total=float(totalBebida+totalEntrada+totalPalomitas)
    pago=float(input(f'Su total a pagar es de {total} \nCon cuanto desea pagar?'))
    if pago>total:
             vuelto=float((pago-total))
             print(f'Su vuelto es de ${vuelto}')
    else:
             print('Monto insuficiente.')
