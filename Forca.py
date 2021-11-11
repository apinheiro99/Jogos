import random

def jogar():
    imprime_abertura()

    palavras = abre_arquivo()
    
    palavra_secreta = palavras[random.randrange(0,len(palavras))]
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    
    while ( not(enforcou) and not(acertou)):
        chute = input("Qual a letra? ").strip().upper()

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[posicao] = letra
                posicao += + 1
        else:
            erros += 1
            print("Você errou a letra e ainda restam {} tentativas".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    elif (enforcou):
        print("Você perdeu!")

def imprime_abertura():
    print("############################")
    print("## Este é o jogo da Forca ##")
    print("############################")

def abre_arquivo():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper())
    return palavras

if (__name__ == "__main__"):
    jogar()
