def calcular_precio(importe, tipo_iva):
    iva = importe * (tipo_iva / 100) 
    precio = importe + iva
    print(f"El precio final del artículo es: {precio}€")

def main():
    importe_convertido = float(input("Introduzca el importe sin IVA del artículo: "))
    iva_convertido = float(input("Introduzca el IVA a aplicar (en porcentaje): "))
    calcular_precio(importe_convertido, iva_convertido)

if __name__ == "__main__":
    main()