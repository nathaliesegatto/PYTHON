print("**********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("**********************************")
print()
print('Você terá algumas chances para acertar o NÚMERO SECRETO.')

pontos = 1000
print()

print('Seus pontos iniciais: ', pontos)

print()
print('Níveis de dificuldade:')
print()
print('(1) Fácil')
print('(2) Médio')
print('(3) Difícil')
print()

nivel = int(input('Digite o número da dificuldade desejada: '))
print ()

while (nivel < 1) or (nivel > 3):
  print ('*** NÍVEL INVÁLIDO! ***')
  print()
  print ('(1) Fácil - 10 tentativas')
  print ('(2) Médio - 5 tentativas')
  print ('(3) Difícil - 3 tentativas')
  print()
  nivel = int(input('Digite o número do nível desejado: '))
  print()


if (nivel == 1):
  tentativas = 10
  print ()
  print ()
elif (nivel == 2):
  tentativas = 5
  print ()
elif (nivel == 3):
  tentativas = 3
  print()

import random
numero_secreto = random.randrange(1,101)
rodada = 1

for rodada in range(1, tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número inteiro entre 1 e 100: '))
    if (chute < 1 or chute > 100):
      print()
      print('O número digitado é inválido.')
      print()
      continue
    else:
      if (chute == numero_secreto):
        print()
        print('Parabéns! Você acertou.')
        print('Total de pontos: ', pontos)
        print()
        break
      else:
        if (chute < numero_secreto):
          print()
          print('*** O número secreto é MAIOR que', chute, '. ***')
          print()
          rodada = rodada + 1
          if (nivel == 1):
            pontos = pontos - 90
          elif (nivel == 2):
            pontos = pontos - 180
          elif (nivel == 3):
            pontos = pontos - 300
          print()
          print('Seus pontos: ', pontos)
        elif (chute > numero_secreto):
          print()
          print('*** O número secreto é MENOR que', chute, '. ***')
          print()
          rodada = rodada + 1
          if (nivel == 1):
            pontos = pontos - 90
          elif (nivel == 2):
            pontos = pontos - 180
          elif (nivel == 3):
            pontos = pontos - 300
            print()
            print('Seus pontos: ', pontos)

if (rodada == tentativas + 1):
  print()
  print ('Número de tentativas excedido.')
  print ('A resposta correta é:', numero_secreto, '.')
  print ('Total de pontos: ', pontos)
  print()
  print('FIM DE JOGO!')
else:
  print ()
  print ('FIM DE JOGO!')