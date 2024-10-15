def calcular_suma(n):
    suma = (n*(n+1))/2
    return f"La suma desde 1 hasta {n} es de {suma}"

def main():
    numero = int(input("Introduce un número entero positivo: "))
    resultado = calcular_suma(numero)
    print(resultado)
    
if __name__ == "__main__":
    main()