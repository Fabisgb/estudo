# listas

# Antes
nota1 = 7.0
nota2 = 9.7
nota3 =8.2

# Com LISTA
# Para se abrir uma lista, se usa colchetes[]

notas = [7.9, 9.7, 8.2]

#Criando LISTAS

# LISTA VAZIA, também se pode criar com o List()
lista = []
lista = list()
lista = [26, 'Fabiana', 3.14159, True]

#Fazendo uma lista de listas
lista_de_lista = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

# Indexação - Acessando um elemento da lista por meio de um índice

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

'''
* Se colocar um índice que não existe? Ele retorna um erro (IndexError: list index out of range - Lista fora da faixa, essa lista não existe.)

print(lista[4])

-1 em uma lista é o último elemento, -2 penúltimo, -3 antepenúltimo e assim sucessivamente.
No Python, você também pode acessar índices negativos

print(lista[-1])
'''

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

# os dois pontos nesse caso está falando que quer os ítens no intervalo de 0 a 3.
print(lista[0:3])
print(lista[3:6])

# quando você não determina até onde vai, ele vai até o final.
print(lista[3:])

# quando você quer pular, nesse exemplo de 2 em 2, coloque a quantidade que vc quer por último dentro do colchetes e antes vem os dois pontos.
print(lista[2:6:2])

# > Interações com FOR

# 1. Utilizando os próprios elementos da lista

# para cada elemento dentro da lista, imprima elemento
for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

# imprimir utilizando o tamanho da lista
# para saber quantos elementos a lista possui, é só usar LEN (LENGTH - COMPRIMENTO)
# Semprre traz a quantidade de elementos que tem dentro da sua lista

print('Comprimento da lista: ', len(lista))

'''
# Usando LEN no RANGE, deixa tudo dinâmico, ele vai colocart todos os elementos da lista.
for i in range(len(lista)):
    print(i)
'''

# Ao invéis de imprimir o 'i', seria imprimir minha lista na posição 'i' pelo o índice.
for i in range(len(lista)):
    print(lista[i])