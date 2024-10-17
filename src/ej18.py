def main():
    nom = input("Escriba su nombre: ")
    apellido_1 = input("Escriba su primer apellido: ")
    apellido_2 = input("Escriba su segundo apellido: ")
    
    print(nom .upper(), apellido_1 .upper(), apellido_2 .upper())
    print(nom .lower(), apellido_1 .lower(), apellido_2 .lower())
    print(nom [0:1] .upper(),apellido_1 [0:1] .upper(), apellido_2 [0:1] .upper())
    
    
if __name__ == "__main__":
    main()