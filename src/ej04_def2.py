def grados_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5 / 9
    celsius = round(celsius, 2)
    return celsius
    
    
def main():
    fahrenheit = float(input("Introduzca una temperatura en grados Fahrenheit: "))
    
    print(f"{grados_celsius(fahrenheit)}ºC ({fahrenheit:.2f}ºF)")
    
    
if __name__ == "__main__":
    main()