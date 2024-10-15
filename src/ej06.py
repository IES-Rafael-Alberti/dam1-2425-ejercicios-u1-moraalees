importe = float(input("Ingrese el importe final del artículo: "))
iva = importe*0.1
iva = round(iva, 2)
importe2 = importe-iva
importe2 = round(importe2, 2)
print(f"El IVA que se ha pagado es de {iva}")
print(f"El importe sin IVA del artículo es de {importe2}")