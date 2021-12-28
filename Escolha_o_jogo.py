import Forca
import Adivinhacao_7

print("**********************************")
print("Bem-vindo!")
print("**********************************")
print()

print ('Escolha seu jogo!')
jogo = int(input('(1) Forca  (2) Adivinhação  (3) Encerrar: '))

while (jogo != 3):
    if (jogo == 1):
        print ()
        Forca.jogar_forca() #necessário usar nome do módulo de onde vem a funcao antes (ex.: random.ramdom())
    elif (jogo ==2):
        print ()
        Adivinhacao_7.jogar_adivinhacao()
    print()
    print('Escolha seu jogo!')
    jogo = int(input('(1) Forca  (2) Adivinhação  (3) Encerrar: '))

print()
print()
print ('*** Volte sempre! ***')



