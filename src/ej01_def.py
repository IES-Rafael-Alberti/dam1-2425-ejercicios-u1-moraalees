def intro_nombre(nombre: str):
    return nombre


def main():
    nombre = input("Introduzca su nombre: ")
    saludo = intro_nombre(nombre)
    print(f"Hola, {saludo}.")

if __name__ == "__main__":
    main()
    