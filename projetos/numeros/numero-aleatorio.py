import random 

numeroAleatorio = random.randint(0, 10)


adivinharNumero = int(input("Número: "))

print(f"Você inseriu o número: {adivinharNumero}")
print(f"O número aleatório era: {numeroAleatorio}")

if numeroAleatorio == adivinharNumero:
    print("voce acertou o numero")

else:
    print("voce errou")