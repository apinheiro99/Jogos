import random

def jogar():
    print("############################")
    print("Este é o jogo de adivinhação")
    print("############################")

    numero_secreto = random.randrange(1,101)
    print(numero_secreto, __name__)

    pontos = 1000

    max = int(input("Entre com o nível: (1) Fácil, (2) Médio, (3) Difícil -> "))
    if (max == 1):
        max = 20
    elif (max == 2):
        max = 10
    else:
        max = 5

    for tentativas in range (1,max+1):
        print("Tentativa {}/{}".format(tentativas, max), "\n")

        numero = input("Digite o seu numero entre 1 e 100 -> ")
        print("Você digitou ", numero, "\n")

        if ((int(numero) < 1) or (int(numero) > 100)):
            print("Digite um numero entre 1 e 100 \n")
            continue

        if (numero_secreto == int(numero)):
            print("Você acertou! :) e fez {} pontos".format(pontos))
            break
        elif (numero_secreto > int(numero)):
            print("Você errou. O numero é maior:(")
        elif (numero_secreto < int(numero)):
            print(("Você errou. O numero é menor :("))

        pontos = pontos - abs(numero_secreto - int(numero))

    print("O numero era {}".format(numero_secreto))

if (__name__ == "__main__"):
    jogar()