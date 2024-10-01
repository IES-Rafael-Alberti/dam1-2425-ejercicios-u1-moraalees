imp = float(input("Ingrese el importe final del artículo: "))
iva = imp*0.1
imp2 = imp-iva
print(f"El IVA que se ha pagado es de {iva}")
print(f"El importe sin IVA del artículo es de {imp2}")