import Adivinhacao
import Forca

print("(1) Adivinhação (2) Forca" )
jogo = int(input("Escolha a opção"))

if (jogo == 1):
    Adivinhacao.jogar()
elif (jogo == 2):
    Forca.jogar()