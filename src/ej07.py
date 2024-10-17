def main():
    num1 = float(input("Introduzca un número: "))
    num2 = float(input("Introduzca otro número: "))
    num3 = float(input("Introduzca un último número: "))
    suma = num1 + num2 + num3
    suma = round(suma, 2)
    
    print(f"La suma de dichos números es de {suma}")
    
    
if __name__ == "__main__":
    main()