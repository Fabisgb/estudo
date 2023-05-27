# Funções

# 1. O que são funções e por que utilizá-las?

'''
print() # - imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() # - retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # - recebe uma lista e retorna o tamanho dessa lista.
max() # - retorna o maior valor de uma lista.
'''

# 2. Criação de Funções

# Função inicial - como criar sua própria função.

# DEF - Define, definir, nesse caso abaixo, uma função.
def saudacao():
    print('Seja Bem vindo(a)!') 
    print('Olá! É um prazer ter você fazendo parte desse curso.') 

saudacao()

# Função com parâmetros

'''
def saudacao(nome):
    print(f'Seja Bem vindo(a)!', (nome,)) 
    print('Olá! É um prazer ter você fazendo parte desse curso.')

saudacao('fabiana')
'''

def saudacao(nome, curso):
    print(f'Seja Bem vindo(a)!', (nome)) 
    print(f'Olá! É um prazer ter você fazendo parte do curso de ', (curso))

saudacao('fabiana', 'Javascript')

# função co parâmetros default

# Depois do curso tem o sinal de igual na DEF, pois você está dizendo que por padrão o nome do curso é Python
def saudacao(nome, curso='Python'):
    print(f'Seja Bem vindo(a)!', (nome)) 
    print(f'Olá! É um prazer ter você fazendo parte do curso de ', (curso))

saudacao('fabiana')

# Funções com retorno

# Sempre que se usa RETURN, nehuma liha de código é mais aceita dentro do paramentro deitico. Observe o comando print.
# Só use o RETURN no final da sua função, pois dali em diante, nada mais acontece.
def soma(num1, num2):
    return num1 + num2
    print
   

resultado = soma(5, 7)

print('O resultado da soma é', resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 +num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 20,)

print(resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 +num2
    elif operacao == '-':
        return num1 - num2

# Para informar que a operção é negativa, é só colocar o menos no final dos números dentro de colchetes.  
resultado = calculadora(10, 20, '-')

print(resultado)
