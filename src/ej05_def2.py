def calcula_precio(importe: float, iva: float) -> str:
    importe = round(importe, 2)
    iva = round(iva, 2)
    return importe+importe*iva/100


def main():
    importe = float(input("Introduzca un importe: "))
    iva = float(input("Introduzca el iva a aplicar: "))
    if (iva < 0 or iva > 100):
        iva = 21
        
    print(f"El precio final del artículo con IVA ({iva}) es {calcula_precio(importe, iva)}€")
    
    
    
if __name__ == "__main__":
    main()