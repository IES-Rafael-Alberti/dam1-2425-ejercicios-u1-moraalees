def main():
    fecha = input("Introduzca su fecha de nacimiento (dd/mm/aaaa): ")
    dia, mes, año = fecha.split("/")
    
    print(f"El día que usted nació fue el {dia} del {mes} del {año}.")
    
    
if __name__ == "__main__":
    main()