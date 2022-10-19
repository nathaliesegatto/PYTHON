"""
Output - print(): Apresenta dados ao usuário
Input - input(): Recebe dados do usuário

Obs.: Todos os dados recebidos são do tipo String.

"""

# print('Digite uma cor: ')
# cor = input()

# print()
# print('Você escolheu', cor, '.')


# #Print versões 2.x
# print ('Você escolheu %s' % cor, '.')

#Print versões 3.x a 3.7
# print('Você escolheu {0}'.format(cor), '.')

#Print versões a partir de 3.7
# print(f'Você escolheu {cor}', '.')

#MAIS UTILIZADOS
# cor = input('Digite uma cor:')
# print(f'Você escolheu {cor}.')


# print('O')
# print('tomate')
# print('é')
# print('vermelho.')
#
# print()
# print('O', end=' ') # esse final já vem pulando 1 linha, se coloco nada, ele preenche o espaço com nada
# print('tomate', end=' $ ') # esse final já vem pulando 1 linha, se coloco $ ele preenche o espaço com $
# print('é', end=' ') # esse final já vem pulando 1 linha, se coloco nada, ele não pula
# print('vermelho\n') # \n faz com que pule uma linha
#
# print('O', end='\n')
# print('tomate', end='\n')
# print('é', end=' ')
# print('vermelho.', end='\n')
#
# cor = input('Digite uma cor: ')
# num = input('Digite um número: ')
#
#
# print()
# #Versões 2.x
# # print('Você escolheu a cor %s e o número %s' % (cor, num), '.')
#
# #Versões 3x a 3.7
# # print('Você escolheu a cor {0} e o número {1}'.format(cor, num), '.')
#
# #Versões a partir de 3.7
# print(f'Você escolheu a cor {cor} e o número {num}.')



#Realizar operações nas saídas (print)

num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
# print(f'A Soma é', {num1 + num2})               # ERRO, NÃO SOMA E SIM CONCATENA
print(f'A soma é: {int(num1) + int(num2)}.')      # CORRETO (CASTING, CONVERSÃO DE UM TIPO DE DADO PARA OUTRO)




