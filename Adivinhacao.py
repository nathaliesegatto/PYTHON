# JOGO DE ADIVINHAÇÃO COM "FOR"
# O usuário pode inserir diversos valores até que acerte o "número secreto".
# Quantidade de tentativas LIMITADAS.
# Função "RANGE", o último valor não é considerado. EX: (1,3) - vai repetir 2 vezes.
# Função "RANGE", é possível incluir passo. EX: (1,10,2) - vai repetir de 1 a 9 a cada 2 números, ou seja, 4 vezes.


print("**********************************")
print()
print("Bem-vindo ao jogo de adivinhação!")
print()
print('Você terá 3 chances para acertar o número secreto.')
print()

numero_secreto = 17
tentativas = 3
rodada = 1

for rodada in range(1, tentativas + 1):
    print('Tentativa {} de {}'.format(rodada,
                                      tentativas))  # Função "FORMAT" (.format(x,y)) para atribuir valores das variáveis aos colchetes.
    chute = int(input('Digite um número inteiro entre 1 e 20: '))
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