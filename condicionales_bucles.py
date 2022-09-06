#CONDICIONALES
x = 2
if x > 10:
    print("Mayor a 10")
else:
    print("Menor a 10")

if x < 10:
    print("Menor a 10")
elif x > 25:
    print("Mayor a 25")
else:
    print("Número entre 10 y 25")

y = 2
if (y < 5 and x > 10): #'and' ambas condicionales se deben de cumplir
    print("Y menor a 5, X mayor a 10")
else:
    print("Alguna de las condicionales no se cumplió")

if(y < 5 or x > 10): #'or' o una u otra de las condicionales se debe cumplir
    print("Alguna de las dos SI se cumplió")
else:
    print("Ninguna de las condicionales se cumplió")


if x < 5:
    print("Menor a 5")


i = 10
if (i > 5 and i % 2 == 0 and i % 5 == 0):
    print("Se cumple con 3")


#BUCLES o CICLOS
for i in range(5): #del 0 al 4. YA NO entra en el 5
    print(i)

print('-----------')

for j in range(1, 5): #del 1 al 4. Ya NO entra en el 5
    print(j)

print('-----------')

for k in range(0, 10, 2): #Comienzo, Parada, Cantidad a avanzar
    print(k)

#Podemos recorrer textos
string = "Buenos días"
for letra in string:
    print(letra)

array = ['A', 'B', 'C', 'D']
# for(var i=0; i<array.lenght;i++) {
#     console.log(array[i])
# }
for elemento in array:
    print(elemento)

gastos = [10, 20, 30, 10]
total = 0
#total = 0
#gasto = 10
#total = 0 + 10 = 10

#gasto = 20
#total = 10 + 20 = 30

#gasto = 30
#total = 30 + 30 = 60

#gasto = 10
#total = 60 + 10 = 70
for gasto in gastos:
    total += gasto # total = total + gasto

print(total)

array = ['A', 'B', 'C', 'D']
for i in range(0, len(array)): #Si quisiéramos saber el índice o posicion de mi arreglo
    print(i, array[i])


diccionario = {"nombre": "Elena", "apellido": "De Troya", "edad": 31}
for llave in diccionario:
    print(llave, diccionario[llave])


y = 0
while y < 3:
    print(y)
    y += 1
else:
    print("Sentencia else final")


num = 1
while num < 15:
    print(num)
    num += 2
# else:
#     print("Ya no entra al ciclo porque el número es", num)

#BREAK: es una interrupción COMPLETA de mi bucle, es decir cuando no encontramos con un break el bucle deja de ejecutarse POR COMPLETO

#CONTINUE: es una interrupción de esa ronda del bucle. Cuando nos encontramos con un continue, el bucle ignora esa ronda y continúa la siguiente

#RETO 1
#Dado un for y recorriendo del 1 al 15, imprime todos los número EXCEPTO aquellos múltiples de 5 - Break o Continue?
#1 - 15
#x = 1
#PRINT 1
#x = 2
#PRINT 2
#x = 3
#PRINT 3
#x = 4
#PRINT 4
#x = 5
#x = 6
for x in range(1, 16):
    if x % 5 == 0:
        continue
    print(x)

#RETO 2
#Dada una cadena, imprime cada uno de los caracteres y DETENTE cuando encuentres un .
cadena1 = "Había una vez una niña. Esa niña quería aprender Python"
for letra in cadena1:
    if letra == ".":
        break
    
    print(letra)


#1-100 cuando sea divisible entre 3 imprima pizza
#divisible entre 7 imprima sandwish
#x = 1
#PRINT 1
#x = 2
#PRINT 2
#x = 3
#PRINT pizza
#x = 4
#PRINT 4
#x = 5
#PRINT 5
#x = 6
#PRINT pizza
#x = 7
#PRINT sandwich
for x in range(1, 101): #
    if x % 3 == 0:
        print("pizza")
    elif x % 7 == 0:
        print("sandwich")
    else:
        print(x)


#FOR con letras
texto = "Hola chicas, 'buenos días'"
#caracter = "H"
#caracter = "o"
#caracter = "l"
#caracter = "a"
print(texto)
for caracter in texto:
    print(caracter)
