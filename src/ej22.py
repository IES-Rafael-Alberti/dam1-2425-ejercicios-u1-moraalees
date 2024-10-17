def main():
    frase = input("Escriba una frase: ")
    vocal = input("Ahora escriba una vocal: ")
    if (vocal != "a" and vocal != "e" and vocal != "i" and vocal != "o" and vocal != "u"):
        print("Eso no es una vocal.")
        
    else:
        print(frase, vocal .upper())    
    
    
if __name__ == "__main__":
    main()