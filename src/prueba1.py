def dame_numero(num1: str, num2: str) -> int:
    num1 = int(input("Introduzca un número: "))
    num2 = int(input("Introduzca otro número: "))
    return num1, num2

def comparador_numeros(num1: str, num2: str) -> int:
    if (num1 == num2):
        return 0
    else:
        if (num1 > num2):
            return num1
        else:
            return num2

def main():
    numero1 = 0
    numero2 = 0
    numero1, numero2 = dame_numero(numero1, numero2)
    comparador_numeros(numero1, numero2)
    
    
if __name__ == "__main__":
    main()