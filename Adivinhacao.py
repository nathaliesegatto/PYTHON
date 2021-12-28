print("**********************************")
print()
print("Bem-vindo ao jogo de adivinhação!")
print()
print('Você terá 3 chances para acertar o número secreto.')
print()

numero_secreto = 17
tentativas = 3
rodada = 1

for rodada in range(1,
                    tentativas + 1):  # O NÚMERO 1 REPRESENTA A PARTIDA, E O ÚLTIMO NÚMERO SERÁ SEMPRE O ANTERIOR AO ESCRITO
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número inteiro entre 1 e 20: '))
    if (chute < 1 or chute > 100):
        print()
        print('O número digitado é inválido.')
        print()
        continue  # O COMANDO CONTINUE RETORNA PARA O INÍCIO DO LAÇO DE REPETIÇÃO.
    else:
        if (chute == numero_secreto):
            print()
            print('Parabéns! Você acertou.')
            print()
            break  # O COMANDO BREAK ENCERRA O LAÇO DE REPETIÇÃO.
        else:
            if (chute < numero_secreto):
                print('O número digitado é menor que o número secreto.')
                print()
                rodada = rodada + 1
            elif (chute > numero_secreto):
                print('O número digitado é maior que o número secreto.')
                print()
                rodada = rodada + 1

if (rodada == tentativas + 1):
    print()
    print('Número de tentativas excedido.')
    print('FIM DE JOGO!')
else:
    print()
    print('FIM DE JOGO!')