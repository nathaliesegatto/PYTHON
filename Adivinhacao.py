print("**********************************")
print()
print("Bem-vindo ao jogo de adivinhação!")
print()
print('Você terá 3 chances para acertar o número secreto.')
print()

numero_secreto = 17
tentativas = 3
rodada = 1

while (rodada <= tentativas):
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número inteiro de 1 a 20: '))
    if (chute == numero_secreto):
      print()
      print('Parabéns! Você acertou.')
      print()
      print('FIM DE JOGO.')
      rodada = (tentativas + 4)
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
 print ()
 print('Número de tentativas excedido.')
 print('FIM DE JOGO!')
elif (rodada <= tentativas):
 print()
 print('FIM DE JOGO!')