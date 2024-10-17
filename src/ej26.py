def main():
    compra = input("Introduzca su compra nombrando artículos separados por comas: ")
    lista = compra.split(",")
    
    print("Su lista de la compra es:")
    for compra in lista:
        print(compra.strip())
    
    
if __name__ == "__main__":
    main()