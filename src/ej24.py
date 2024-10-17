def main():
    precio = input("Escriba un precio de un producto en euros: ")
    euros, centimos = precio.split(".")
    
    print(f"Lo que ha pagado por ese producto es de {euros}€ con {centimos} céntimos.")
    
    
if __name__ == "__main__":
    main()