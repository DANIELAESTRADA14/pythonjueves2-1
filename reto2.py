#Multiplo de 5
numero = int(input("Ingrese un numero: "))
modulo = numero % 5
#print(f"El modulo del numero es {modulo}")

#Condiciones en python
if modulo == 0:
    print(f"El numero {numero} es multiplo de 5")
else:
    print(f"El numero {numero} no es multiplo de 5")
print("fin del programa")

#Simplificado (se puede hacer on if and else)
def es_multiplo(numero,multiplo):
    return numero % multiplo == 0 

resultado = es_multiplo(15,5)
print(resultado)