#EJERCICIO 1: Suma de pares positivos
def EJERCICIO_1():
  total= 0
  for a in range(5): 
        a = int(input("Ingrese un numero: "))
        if (a > 0 and a % 2 == 0):
            total += a
  print("La suma de los números pares positivos es:", (total))


#EJERCICIO 2: Clasificacion de edad
def EJERCICIO_2():
EJ2=int(input("ingrese su edad: "))
if(EJ2<=13):
  print("Niño")
elif(13<EJ2<=17):
  print("Adolescente")
elif(18<EJ2<=59):
  print("Adulto")
else:
  print("Adulto mayor")


#EJERCICIO 3: Contador de vocales
def EJERCICIO_3():
p= input("ingrese una palabra: ")
a=p.count("a")+ p.count("A")
e=p.count("e")+ p.count("E")
i=p.count("i")+ p.count("I")
o=p.count("o")+ p.count("O")
u=p.count("u")+ p.count("U")
print("La palabra tiene: ")
print(f"a:", (a) )
print(f"e:", (e) )
print(f"i:", (i) )
print(f"o:", (o) )
print(f"u:", (u) )
