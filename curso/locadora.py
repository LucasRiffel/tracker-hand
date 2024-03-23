import os

carros = [
            ("chevrolet tracker" , 120),
            ("chevrolet onix" , 90),
            ("chevrolet spin" , 150),
            ("hyundai hb20" , 85),
            ("hyundai tucson" , 120),
            ("fiat uno" , 60),
            ("fiat mobi" , 70),
            ("fiat pulse" , 130)
         ]
alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /Dia.".format(i, car[0], car[1]))
        
mostrar_lista_de_carros(carros)    

while True: 
    os.system('cls')
    print("======")
    print("Bem-vindo à locadora de carros!")
    print("======")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())

    os.system('cls')
    if op == 0: 
       mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("Por quantos dias você quer alugar esse carro?")
        dias = int(input())
        os.system('cls')

        print("Você escolheu {} por {} dias.".format(carros[cod_car][0], dias))
        print("O aluguel totalizaria R$ {}. deseja alugar?".format(dias * carros[cod_car][1]))
        
        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print("Não há mais carross para devolver.")
        else:    
            print("Segue a lista de carros alugados. Qual você quer devolver?")
            mostrar_lista_de_carros(alugados)
            print("") 
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:  
                print("Obrigado por devolver o carro {}.".format(alugados[cod_car][0]))
                carros.append(alugados.pop(cod_car))
              
    print("")
    print("======")
    print(" 0 - CONTINUAR | 1 - SAIR")
    if float(input()) == 1: 
        break