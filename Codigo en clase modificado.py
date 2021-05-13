salir = False
opcion = 0

while not salir:

  print ("Bienvenido")
  print ("1. Ingresar sesión")
  print ("2. Registrar usuario")
  print ("3. Salir")
   
  print ("Elige una opcion")
  correcto=False
  num=0

  while(not correcto):
    try:
      num = int(input("Introduce un numero entero: "))
      correcto=True
    except ValueError:
      print('Error, introduce un numero entero')
  opcion=num

  if opcion == 1:
    print ("Ha seleccionado la Opcion 1")

  elif opcion == 2:
    print ("Ha seleccionado la Opcion 2")

  elif opcion == 3:
    salir = True

  else:
    print ("Introduce un numero entre 1 y 3")
