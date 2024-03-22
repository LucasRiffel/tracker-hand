def calcular():
    while True:
        operacao = int(input("Escolha a operação (0 = soma, 1 = subtração, 2 = multiplicação, 3 = divisão, 4 = exponenciação): "))
        if operacao not in [0, 1, 2, 3, 4]:
            print("Operação inválida.")
            continue

        num1 = float(input("Escolha o primeiro número: "))
        num2 = float(input("Escolha o segundo número: "))

        if operacao == 0:
            resultado = num1 + num2
            print("O resultado da soma é:", resultado)
        elif operacao == 1:
            resultado = num1 - num2
            print("O resultado da subtração é:", resultado)
        elif operacao == 2:
            resultado = num1 * num2
            print("O resultado da multiplicação é:", resultado)
        elif operacao == 3:
            resultado = num1 % num2
            print("O resultado da subtração é:", resultado)
        elif operacao == 4:
            resultado = num1 ** num2
            print("O resultado da multiplicação é:", resultado)

        outra_operacao = input("Deseja fazer outra operação? (sim/não): ").lower()
        if outra_operacao != "sim":
            print("Programa encerrado.")
            exit()
           
calcular()
