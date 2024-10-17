def main():
    celsius = float(input("Introduzca la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    fahrenheit = round(fahrenheit, 2)
    
    print(f"La temperatura en grados Fahrenheit es {fahrenheit}ºF ({celsius}ºC).")


if __name__ == "__main__":
    main()