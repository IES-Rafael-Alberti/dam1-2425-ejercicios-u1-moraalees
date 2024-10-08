def main():
    nombre = input("Escriba el nombre de su producto: ")
    precio = float(input("Escriba el precio de su producto: "))
    num = int(input("Introduzca ahora un número de unidades: "))
    total = precio * num
    
    print(f"Nombre: {nombre} - Precio unitario: {precio:8.2f} - Nº unidades: {num:03d} - Coste total: {total:10.2f}")
    
if __name__ == "__main__":
    main()