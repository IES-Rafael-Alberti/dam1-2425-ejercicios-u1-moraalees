def main():
    n = int(input("Introduzca un número entero como dividendo: "))
    m = int(input("Introduzca otro número entero como divisor: "))
    while (m == 0):
        print("El divisor no puede ser 0")
        m = int(input("Introduzca otro número entero: "))
        
    c = n/m
    r = n%m
    print(f"La división de {n} entre {m} da un cociente {c} y un resto {r}")
    
    
if __name__ == "__main__":
    main()