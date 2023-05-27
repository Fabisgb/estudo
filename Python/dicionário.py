# > Dicionários

# criando dicionários

dicionario ={}

# dicionário vazio
dicionario = dict()

# dicionário já com conteúdo
dicionario = {'nome': 'Fabiana', 'idade': 26, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador'] = True

print(dicionario)

# Obs.: Se já existe um conteúdo e vc pede para adicionador outro valor naquele conteúdo, irá sbreescrever.
dicionario['altura'] = 2

print(dicionario)

# Iterando sobre um dicionário - percorrendo pelo dicionário

# Percorrendo pelas as chaves e não as respostas
for chave in dicionario:
    print(chave, dicionario[chave])


# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)



