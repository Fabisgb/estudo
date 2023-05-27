# > VARIÁVEIS

# 1. Variáveis

idade = 26 # aqui estou criando uma variável, = se lê, RECEBE e não igual.
'''
O QUE ÉSTÁ ESCRITO DO LADO DIREITO DO SINAL DE =, VAI SER ATRIBUÍDO A SUA VARIÁVEL DO LADO ESQUERDO,
QUE NESSE CASO É IDADE.
'''

print(idade)

nome = 'Fabiana'

print(nome)


'''
    Tipos de Variáveis

    1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
    2. float: números reais, ou seja, números com parte decimal: 1.0, -2,7, 3.14
    3. str: cadeias de caracteres, ou seja, dados textuais (string)
    4. bool: valores lógicos (booleanos) true ou false  (0 ou 1)
'''
idade = 26 # int
altura = 1.77 # float
nome = 'Fabiana' # str
estudando = True # True ou False sempre se escreve com a primeira letra Maiúscula

# type é usado para imprimir os tipos de variáveis e não a informação final 
print( type(idade) ) 
print( type(altura) )
print( type(nome) )
print( type(estudando) )


# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando?')

# A vírgula imprime todas as variáveis, é só ir separando por vírgulas
print('A limguagem que você está estudando é' , linguagem)



# Imprimindo variáveis + Mais sobre a função print