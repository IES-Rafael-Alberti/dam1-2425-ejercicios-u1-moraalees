def saludo(nom):
    return "Hola, " + nom + "."


def main():
    nombre = input("Introduzca su nombre: ")
    print(saludo(nombre))
    
if __name__ == "__main__":
    main()