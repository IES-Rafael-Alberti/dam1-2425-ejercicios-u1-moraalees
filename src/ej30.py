def main():
    numero_inicio = int(input("Introduzca un número entero: "))
    incremento = int(input("Introduzca un incremento que vaya sumando la serie (mayor que 0): "))
    total_serie = int(input("Introduzca la cantidad de números que van a salir en la serie (mayor que 0): "))
    
    while (incremento < 0):
        print("ERROR - El incremento debe ser mayor que 0.")
        incremento = int(input("Introduzca un incremento que vaya sumando la serie (mayor que 0): "))
        
    while (total_serie < 0):
        print("ERROR - El total de la serie debe ser mayor que 0.")
        total_serie = int(input("Introduzca la cantidad de números que van a salir en la serie (mayor que 0): "))
    
    cont = 0
    while (cont < total_serie-1):
        cont = cont + 1
        print(f"{numero_inicio}-", end="")
        numero_inicio = numero_inicio + incremento
        
    while (cont < total_serie):
        cont = cont + 1
        print(f"{numero_inicio}", end="")
        numero_inicio = numero_inicio + incremento          
  
    
if __name__ == "__main__":
    main()