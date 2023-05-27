numero_sorteado = 15

numero_escolhido = int(input('informe um número entre 1 e 20: '))

'''
O WHILE substitui esse código, pois precisamos que o usuário digite novamente outro número,
e usando IF e ELSE, isso não ocorre, simplismente para em "Você Errou!"

# Quando você quiser comparar qualquer coisa, se usa dois sinais de igual juntos
# Um único sinal de igual é uma atribuição.
# O sinal de dois pontos, significa então

if numero_sorteado == numero_escolhido:
    print('Vicê Acertou!')
else:
    print('Você errou!')
'''
# While, significa enquanto.
# Os sinais de exclamação e igual juntos, significa diferente.

while numero_escolhido != numero_sorteado:
    print ('Você errou o número, tente novamente...')

    numero_escolhido = int(input('informe um número entre 1 e 20: '))

print('Parabéns! Você acertou!')

'''
* Observação: nunca se esqueça de dizer até onde o while tem que ir,
pois ele ficará exibindo a informação de "Você errou... novamente" infinitamente.
por isso logo abaixo do print tem a linha de código do numero_escolhido.
'''

# Exemplo 2 - Estrutura com Contador

contador = 0

while contador < 5:
    print(contador)

    # A cada Laço, repetição, vai acrescentado + 1 ao contador
    contador = contador + 1