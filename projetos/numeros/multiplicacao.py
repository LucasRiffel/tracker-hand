
while True:
    try:
        Numero1 = int(input("escolha o numero 1: "))

        Numero2 = int(input("escolha o numero 2: "))

        Resultado = Numero1 * Numero2
        print(Resultado)
        continuar = input("Quer continuar?(sim/nao)")
        if continuar != "sim":
            break
    except ValueError:
        print("Erro")    

    