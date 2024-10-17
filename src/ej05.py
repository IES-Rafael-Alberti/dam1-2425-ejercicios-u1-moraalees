def main():
    importe = float(input("Introduzca el importe sin IVA del artículo: "))
    iva = float(input("Introduzca el IVA a aplicar (en porcentaje): "))
    total = importe + (importe*iva/100)
    total = round(total, 2)
    
    print(f"El precio final del artículo es: {total}€")
    

if __name__ == "__main__":
    main()