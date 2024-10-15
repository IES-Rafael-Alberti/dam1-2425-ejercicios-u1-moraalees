import random


def dame_un_numero_aleatorio(min, max):
    return random.randint(min, max)


def main():
    min = int(input("Dame un número mínimo: "))
    max = int(input("Dame un número máximo: "))
    
    num_aleatorio = dame_un_numero_aleatorio(min, max)
    print(num_aleatorio)


if __name__ == "__main__":
    main()