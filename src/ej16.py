def main():
    pan_no_dia = int(input("Introduzca el número de barras vendidas que no son del día: "))
    pan_dia = 3.49
    total = pan_no_dia*60/100
    
    print(f"Una barra de pan del día cuesta {pan_dia}€, el descuento que se te hace por no ser fresca es del 60%, por tanto el precio a pagar es de {total}€")
    
    
if __name__ == "__main__":
    main()