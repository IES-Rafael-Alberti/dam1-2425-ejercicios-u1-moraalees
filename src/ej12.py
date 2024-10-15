peso = float(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en m: "))
indice = peso/(altura)**2
indice = round(indice, 2)
print(f"Tu índice de masa corporal es {indice}")