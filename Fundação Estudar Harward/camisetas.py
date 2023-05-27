N = int(input("Quantos são os premiados?"))
tamanhos = list(map(int, input().split()))
P = int(input('Quantas camisas P?'))
M = int(input('Quantas camisas M?'))

if 1 <= N <= 1000 and 0 <= P <= 1000 and 0 <= M <= 1000 and N <= P + M:
    tamanho_pequeno = tamanhos.count(1)
    tamanho_medio = tamanhos.count(2)

    if tamanho_pequeno <= P and tamanho_medio <= M:
        print('S')
    else:
        print('N')

