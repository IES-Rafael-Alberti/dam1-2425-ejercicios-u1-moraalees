def main():
    importe_con_iva = float(input("Ingrese el importe final del artículo: "))
    iva = importe_con_iva*0.1
    iva = round(iva, 2)
    importe_sin_iva = importe_con_iva-iva
    importe_sin_iva = round(importe_sin_iva, 2)
    
    print(f"El IVA que se ha pagado es de {iva}%")
    print(f"El importe sin IVA del artículo es de {importe_sin_iva}€")
    

if __name__ == "__main__":
    main()