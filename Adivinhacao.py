print ("**********************************")
print()
print ("Bem-vindo ao jogo de adivinhação!")
print()
print ("**********************************")

numero_secreto = 7
chute = int (input("Digite um número inteiro: "))
print()

while (chute != numero_secreto):
  if (chute > numero_secreto):
    print()
    print ('O número digitado é maior que o número secreto!')
    print()
    chute = int (input('Digite outro número inteiro: '))
  else:
    print ()
    print ('O número digitado é menor que o número secreto!')
    print ()
    chute = int (input('Digite outro número inteiro: '))

print()
print ('***** Muito bem, você acertou!*****')

print ()
print ('FIM DO JOGO.')