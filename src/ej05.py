imp = float(input("Ingrese el importe del artículo: "))
iva = float(input("Ingrese el porcentaje de IVA a aplicar: "))
tot = imp + (imp*iva/100)
print(f"El precio final del artículo es {tot}")