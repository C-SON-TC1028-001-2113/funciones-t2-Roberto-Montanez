def calcula_grado(numero): 
    if numero<=1 and numero>=0 :
        if numero>0.9 :
            return 'A'
        elif numero>0.8 :
            return 'B'
        elif numero>0.7 :
            return 'C'
        elif  numero>0.6 :
            return 'D'
        elif numero<0.6 :
            return 'F'
    else:
        return('score incorrecto')
def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
