def main():
    capital = float(input("Introduzca su cantidad de dinero depositada en la cuenta de ahorros: "))
    i = 4
    capital = capital * (1 + i/100)
    capital = round(capital, 2)
    print(f"La cantidad de ahorros tras el primer año será de {capital}")
    capital = capital * (1 + i/100)
    capital = round(capital, 2)
    print(f"La cantidad de ahorros tras el segundo año será de {capital}")
    capital = capital * (1 + i/100)
    capital = round(capital, 2)
    print(f"La cantidad de ahorros tras el tercer año será de {capital}")
    
    
if __name__ == "__main__":
    main()