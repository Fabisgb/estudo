# CONVERSÃO DE TIPOS

# Os números estão dentro de strings (str - Textos)
idade = '26'
numero1 = '10'
numero2 = '20'

print(numero1 + numero2) 
''' Se mandar assim, como os numeros estão escritos
em formato de texto, o computador faz uma concatenação,
não a soma.
'''

idade_inteira = int(idade)

print(idade, type(idade))

print(idade_inteira, type(idade_inteira) )

# Códigos que se usam com print

# int()- converte qualquer coisa para um inteiro
# str()- converte qualquer tipo de variável para string
# float()- converte qualquer variável para float
# bool()- converte qualquer variável para booleano

altura = float(input('informe a sua altura:'))
print(altura, type(altura))


