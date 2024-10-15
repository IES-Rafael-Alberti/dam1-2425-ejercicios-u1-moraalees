def saludo(nom):
    return "Hola, " + nom + "."

def intro_nombre():
    return input("Introduzca su nombre: ")

def main():
    nombre = intro_nombre
    print(saludo(nombre))
    
if __name__ == "__main__":
    main()