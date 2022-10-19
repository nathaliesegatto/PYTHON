"""

VARIÁVEIS
São um modo de rotular ou nomear todos os dados pertencentes ao seu programa.

DADOS
São todas as informações que serão utilizadas ao longo do seu código, podendo ser números, palavras, frases, textos, dentre outros.

1) Variável Global: podem ser manipuladas ao longo de todo o código.
2) Varável Local: São variáveis que podem ser manipuladas apenas em determinada parte do programa.

REGRAS:
1) Em nomes compostos, separar por underline ou letras maiúsculas;
2) Não devem possuir caracteres especiais;
3) Não podem possuir apenas números no nome;
4) Não podem iniciar com números.

TIPOS DE DADOS:
1) Int: não possuem casas decimais;
2) Float: possuem casas decimais (separadas por PONTO);
3) Complex: números reais acompanhados por números imaginários;
4) Bool: verdadeiro (1 - true) ou falso (0 - false).
5) String: caracteres (entre aspas simples, duplas ou triplas).


Função type(): retorna o tipo do dado/variável.

para imprimir string ao contrário: print(<variavel_string>[::-1])

"""

# idade = 27
# print(type(idade))

# precoBanana = 5.99
# print(type(precoBanana))

# var_complex = 1j
# print(type(var_complex))

#IMPRIMIR VARIÁVEL STRING AO CONTRÁRIO
# nome = "Nathalie"
# print(nome[::-1])

#IMPRIMIR APENAS PARTE DE UMA STRING
# Tom Cruise
# 0123456789
var_string = 'Tom Cruise'
print(var_string[4:10]) # IMPRIME DA POSIÇÃO 4 ATÉ 9 (O 10 NÃO ENTRA)

# DECLARAR MUITAS VARIÁVEIS NA MESMA LINHA
a1,a2,a3,a4,a5 = 1,2.5,True, 2j, 'sim'