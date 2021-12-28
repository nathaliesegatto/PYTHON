# JOGO DE ADIVINHAÇÃO COM - USANDO A FUNÇÃO RANDOM
# O usuário pode inserir diversos valores até que acerte o "número secreto".
# Quantidade de tentativas LIMITADAS.
# Função "RANGE", o último valor não é considerado. EX: (1,3) - vai repetir 2 vezes.
# Função "RANGE", é possível incluir passo. EX: (1,10,2) - vai repetir de 1 a 9 a cada 2 números, ou seja, 4 vezes.
# Função "FORMAT" (.format(x,y)) aplicada na linha 18 para atribuir valores das variáveis aos colchetes.
# A função Random não faz parte do "Built In", é necessário importar (import random)
# O número "random.random" vem entre 0 e 1 com casas decimais, é necessário multiplicá-lo por 100 e usar o arredondamento (round)
# https://docs.python.org/3/library/random.html

print("**********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("**********************************")
print()
print('Qual o nível de dificuldade desejado? ')
print('(1) Fácil')
print('(2) Médio')
print('(3) Difícil')
print()

nivel = int(input('Digite a opção desejada: '))
print()

while (nivel < 1):
    print()
    print('** NÍVEL INVÁLIDO! **')
    print()
    print('(1) Fácil')
    print('(2) Médio')
    print('(3) Difícil')
    print()
    nivel = int(input('Digite a opção desejada: '))
    print()

while (nivel > 3):
    print()
    print('** NÍVEL INVÁLIDO! **')
    print()
    print('(1) Fácil')
    print('(2) Médio')
    print('(3) Difícil')
    print()
    nivel = int(input('Digite a opção desejada: '))
    print()

if (nivel == 1):
    import random

    numero_secreto = random.randrange(1,
                                      11)  # O número "random.randrange" exige parâmetro (entre 1 e 101 nesse caso, pois considera o número anterior ao digitado)
    tentativas = 3
    rodada = 1

    for rodada in range(1,
                        tentativas + 1):  # O NÚMERO 1 REPRESENTA A PARTIDA, E O ÚLTIMO NÚMERO SERÁ SEMPRE O ANTERIOR AO ESCRITO
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input('Digite um número inteiro entre 1 e 10: '))
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
                    print()
                    print('*** O número secreto é MAIOR que', chute, ' ***')
                    print()
                    rodada = rodada + 1
                elif (chute > numero_secreto):
                    print()
                    print('*** O número secreto é MENOR que', chute, ' ***')
                    print()
                    rodada = rodada + 1

    if rodada == tentativas + 1:
        print()
        print('Número de tentativas excedido.')
        print('A resposta correta é:', numero_secreto, '.')
        print('FIM DE JOGO!')
    else:
        print()
        print('FIM DE JOGO!')
elif (nivel == 2):
    import random

    numero_secreto = random.randrange(1,
                                      51)  # O número "random.randrange" exige parâmetro (entre 1 e 101 nesse caso, pois considera o número anterior ao digitado)
    tentativas = 3
    rodada = 1

    for rodada in range(1,
                        tentativas + 1):  # O NÚMERO 1 REPRESENTA A PARTIDA, E O ÚLTIMO NÚMERO SERÁ SEMPRE O ANTERIOR AO ESCRITO
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input('Digite um número inteiro entre 1 e 50: '))
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
                    print()
                    print('*** O número secreto é MAIOR que', chute, ' ***')
                    print()
                    rodada = rodada + 1
                elif (chute > numero_secreto):
                    print()
                    print('*** O número secreto é MENOR que', chute, ' ***')
                    print()
                    rodada = rodada + 1

    if (rodada == tentativas + 1):
        print()
        print('Número de tentativas excedido.')
        print('A resposta correta é:', numero_secreto, '.')
        print('FIM DE JOGO!')
    else:
        print()
        print('FIM DE JOGO!')
elif (nivel == 3):
    import random

    numero_secreto = random.randrange(1, 101)
    tentativas = 3
    rodada = 1
    for rodada in range(1,
                        tentativas + 1):  # O NÚMERO 1 REPRESENTA A PARTIDA, E O ÚLTIMO NÚMERO SERÁ SEMPRE O ANTERIOR AO ESCRITO
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input('Digite um número inteiro entre 1 e 100: '))
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
                    print('*** O número secreto é MAIOR que', chute, ' ***')
                    print()
                    rodada = rodada + 1
                elif (chute > numero_secreto):
                    print('*** O número secreto é MENOR que', chute, ' ***')
                    print()
                    rodada = rodada + 1
    if (rodada == tentativas + 1):
        print()
        print('Número de tentativas excedido.')
        print('A resposta correta é:', numero_secreto, '.')
        print('FIM DE JOGO!')
    else:
        print()
        print('FIM DE JOGO!')
