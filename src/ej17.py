def main():
    nombre = input("Escriba su nombre: ")
    numero = int(input("Ahora escriba cuántas veces quiere que aparezca su nombre en consola: "))
    suma = 0 
    while (suma < numero):
        suma = suma + 1
        print(nombre)
        
        
if __name__ == "__main__":
    main()