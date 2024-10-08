peso = float(input("Introduzca su peso en kg: "))
est = float(input("Introduzca su altura en m: "))
ind = peso/(est)**2
ind = round(ind, 2)
print(f"Tu índice de masa corporal es {ind}")