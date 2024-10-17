def main():
    n = int(input("Introduzca un número positivo entero: "))
    while (n < 1):
        print("El número debe ser mayor que 0.")
        
    suma = (n*(n+1))/2
    
    print(f"La suma de todos los números enteros desde 1 hasta {n} es de: {suma}")


if __name__ == "__main__":
    main()