menu = """
Menu 
1.Suma
2.Resta
3.Multiplicacion
4.Division
5.Salir 
"""
pop = True
while pop == True:
    try:
        print(menu)
        op = int(input("Escoja una operacion:"))
        if op == 1:
            numero1 = float(input("Inserte el primer Numero: "))
            numero2 = float(input("Inserte el segundo numero: "))
            suma = numero1 + numero2
            print("la suma es:", suma)
        elif op == 2:
            numero1 = float(input("Inserte el primer Numero: "))
            numero2 = float(input("Inserte el segundo numero: "))
            resta = numero1 - numero2
            print("la resta es: ", resta)
        elif op == 3:
            numero1 = float(input("Inserte el primer Numero: "))
            numero2 = float(input("Inserte el segundo numero: "))
            multi = numero1 * numero2
            print("la multiplicacion es:", multi)
        elif op == 4:
            numero1 = float(input("Inserte el primer Numero: "))
            numero2 = float(input("Inserte el segundo numero: "))
            try:
                division = numero1 / numero2
                print("la division es:", division)
            except ZeroDivisionError as e:
                print("La division dentro de cero no es permitida")
        elif op == 5:
            pop = False
            print("Gracias por utilizar la calculadora")
        else:
            print("Opcion no valida")
    except ValueError as i:
        print("Caracter no permitido")