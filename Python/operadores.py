# operações Matemáticas (Aritméticas)

'''
    - soma: +
    - subtração: - 
    - multiplicação: *
    - divisão: /
    - divisão inteira: //
    - resto da divisão: %
    - potência: **
'''

numero1 = 10
numero2 = 20

print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
# Divisão inteira, o computador descarta a parte decimal e fica só o número inteiro
print(numero1 // numero2)
# Qual é o resto da divisão de 20 por 3, usa-se MOD
print(20 % 3) # O simbolo de porcentagem, se lê MOD
# potenciação, no lado esquerdo é o número base e no lado direito o expoente. 
print(2 ** 3)

# OPERADORES BOOLEANOS (OU DE COMPARAÇÃO OU LÓGICOS)

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade2)        # false, > é sinal de maior
print(idade1 <= idade2)       # true, <= é sinal de menor e igual
print('Python' == 'python')   # false == é sinal de igual
print('banana' != 'abacaxi')  # true != é sinal de é diferente
print(altura1 >= altura2)     # true >= é sinal de maior e igual
print(altura2 < altura3)      # false > é sinal de maior