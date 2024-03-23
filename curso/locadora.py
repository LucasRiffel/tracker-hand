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

print("======")
print("Bem-vindo à locadora de carros!")
print("======")

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /Dia.".format(i, car[0], car[1]))
        
mostrar_lista_de_carros(carros)    

while True: 
    os.system("clear")

