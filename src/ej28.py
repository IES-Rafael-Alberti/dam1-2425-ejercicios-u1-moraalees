def main():
    num1 = int(input("Escriba un número: "))
    num2 = int(input("Escriba otro número: "))
    if (num1 == num2):
        print("Los números no pueden ser iguales.")
    else:
        if (num1 > num2):
            resta = num1 - num2
            print(f"El número menor es el {num2} y entre ellos existen {resta} números enteros.")
        else:
            resta = num2 - num1
            print(f"El número menor es el {num1} y entre ellos existen {resta} números enteros.")


if __name__ == "__main__":
    main()