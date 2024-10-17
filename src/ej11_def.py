def calcular_suma(n):
    suma = (n*(n+1))/2
    return suma


def main():
    numero = int(input("Introduce un número entero positivo: "))
    
    print(f"La suma desde 1 hasta {numero} es de {calcular_suma(numero)}")
    
    
if __name__ == "__main__":
    main()