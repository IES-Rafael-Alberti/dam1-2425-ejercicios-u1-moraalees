def main():
    num = input("Escriba su número de teléfono junto a su prefijo (+34-) y su extensión (-xx): ")
    num = num.split("-")[1]
    
    print(f"Su número de tfno. sin extensiones ni prefijos es {num}")
    
    
if __name__ == "__main__":
    main()