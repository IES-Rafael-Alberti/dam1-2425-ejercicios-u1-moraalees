def comprobar_entero(cadena : str) -> bool:
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())
    
def dame_entero() -> int:
    cadena = input("Dame un entero: ")
    while not comprobar_entero(cadena):
        cadena = input("\nERROR - Eso no es un número entero\n\nDame un número entero de verdad: ")

    return int(cadena)

def main():
    num = dame_entero()
    print(f"Escribiste el número {num}")


if __name__ == "__main__":
    main()