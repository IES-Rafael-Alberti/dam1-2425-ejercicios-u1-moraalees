def main():
    num = float(input("Introduzca un número: "))
    num += float(input("Introduzca otro número: "))
    num += float(input("Introduzca un último número: "))
    num = round(num, 2)
    print(f"La suma de esos número es: {num}")
    
if __name__ == "__main__":
    main()