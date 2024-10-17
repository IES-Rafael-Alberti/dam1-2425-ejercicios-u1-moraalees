def main():
    nombre = input("Escriba su nombre: ")
    edad = int(input("Escribe su edad: "))
    
    if not nombre:
        nombre = "Desconocido"
   
    while (edad < 0 or edad > 125):
        print("Usted no tiene esa edad, introduzca su edad verdadera: ")
        edad = int(input("Escribe su edad: "))
    
    años = 125 - edad
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años} años por cumplir.")
    
    
if __name__ == "__main__":
    main()