numeroUno=int(input('digite nuemrmo uno; '))
numeroDos=int(input('Digita un segundo numero'))
print(f'el numero es:{numeroUno} ')
print(f'el numero es:{numeroDos} ')
suma=numeroUno+numeroDos
print(f'la suma es {suma}')


#ejercisio numero 1 :
numero = int(input("Ingresa un número: "))
if numero % 5 == 0:
    print(numero, "es múltiplo de 5")
else:
    print(numero, "no es múltiplo de 5")

#ejercisio Numero 2:
numero = int(input("Introduce un número: "))
if numero % 3 == 0:
    print("El número es múltiplo de 3")
else:
    print("El número no es múltiplo de 3")

#ejercisio Numero 3:
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print("El primer número es mayor que el segundo número.")
elif num2 > num1:
    print("El segundo número es mayor que el primer número.")
else:
    print("Los dos números son iguales.")
    
    
#ejerciso Numero 4:
juan = float(input("Introduce la cantidad de dinero que tiene Juan: "))
camila = juan / 2
ricardo = (juan + camila) / 2
total = juan + camila + ricardo

print("Juan tiene", juan, "pesos")
print("Camila tiene", camila, "pesos")
print("Ricardo tiene", ricardo, "pesos")
print("En total, los tres tienen", total, "pesos")


#ejercisio Numero 5:
salario_base = 3500000
comision = 1500000
impuestos = 0.05

ventas = int(input("Introduce el número de licencias de software vendidas: "))
salario_total = salario_base + (comision * ventas)
salario_neto = salario_total * (1 - impuestos)

print("El salario total del vendedor es:", salario_total)
print("El salario neto del vendedor es:", salario_neto)
    
