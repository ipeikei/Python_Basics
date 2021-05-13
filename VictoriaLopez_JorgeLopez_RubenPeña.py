print('Que edad tienes?');
edad=int(input());
if edad>=18:
        print('Eres mayor de edad');
else:
        print('Eres menor de edad');

################
User1='Pedro';
Contrasena1='1234';
User2='Angel';
Contrasena2='a2s1';

print('Ingrese su usuario');
User=input('');
print('Ingrese su contraseña');
Contrasena=input('');

if User==User1 and Contrasena==Contrasena1:
        print('Bienvenido Pedro');
else:
        if User==User2 and Contrasena==Contrasena2:
                print('Bienvenido Angel');
        else:
                print('Usuario Incorrecto, ingrese un usuario y contraseña correcto');

###############
print('Calcularemos tu promedio! \nIngrese su primera nota:');
nota1=float(input());
print('Ingrese segunda nota');
nota2=float(input());
print('Ingrese su tercera nota');
nota3=float(input());
if nota1<=7 and nota2<=7 and nota3<=7:
        print=('La escala de notas es del 1 al 7');
else:
        x=(nota1+nota2+nota3)/3;
        if x>= 4.0:
                print(f'Su promedio es: {x}\nUsted aprobo el ramo');
        else:
                print('Usted reprobo el ramo');

############
print('¿Cuál de los siguientes animales vive en el agua? (Responder con el numero)\n\t1.Perro \n\t2.Cocodrilo \n\t3.Conejo \n\t4.Tiburón');
resp=int(input());
puntaje=0;
if resp==2:
        puntaje=puntaje+0.5;
        print('Acumulaste +0.5 puntos');
elif resp==4:
        puntaje=puntaje+1.0;
        print('Acumulaste +1.0 puntos');
else:
        print('No obtuviste puntos');

print('Vamos de nuevo\n¿Cuál de los siguientes animales vive en el agua? (Responder con el numero)\n\t1.Perro \n\t2.Cocodrilo \n\t3.Conejo \n\t4.Tiburón');
resp=int(input());
if resp==2:
        puntaje=puntaje+0.5;
        print('Acumulaste +0.5 puntos');
elif resp==4:
        puntaje=puntaje+1.0;
        print('Acumulaste +1.0 puntos');
else:
        print('No obtuviste puntos');
        
###########
print('¿Cuál de los siguientes es un personaje de DC? (Responder con el numero)\n\t1.The Punisher \n\t2.Zatanna \n\t3.Peter Parker \n\t4.Pepper');
answr=int(input());
points=0;
if answr==2:
        points=points+1.0;
else:
        points=points+0;

print('¿Cuál de los siguientes fue Robin en el pasado? (Responder con el numero)\n\t1.Jason Todd \n\t2.Arthur Curry \n\t3.Barry Allen \n\t4.Richard Grayson');
answr=int(input());
if answr==1:
        points=points+1.0;
elif answr==4:
        points=points+1.0;
else:
        points=points+0;

print('¿Cuál de los siguientes no pertenece a los jovenes titanes? (Responder con el numero)\n\t1.Damian Wayne \n\t2.Wally West \n\t3.Billy Batson \n\t4.Garfield Logan');
answr=int(input());
if answr==3:
        points=points+1.0;
else:
        points=points+0;

print('Tu puntaje final fue:',points);
