def importe(horas, coste):
    return horas * coste


def main():
    tiempo = int(input("Horas de trabajo: "))
    dinero = int(input("Coste por hora: "))
    importe_total = importe(tiempo, dinero)
    print(f"Importe total: {importe_total}")
    
    
if __name__ == "__main__":
    main()
    