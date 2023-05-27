# Na variável, você pode utilizar qualquer palavra, mas o mais usado é a letra i

# TRADUÇÃO/LÊ-SE: para variavél dentro do (range(10) - FAIXA), faça tal coisa.
# dentro desta faixa de 0 a 9, eu quero que você computador execute um determinado trecho de código.  

'''
for variavel in range(10):
    print(variavel)

* Se eu quizer que comece pelo 1 e não por 0.

* Determine que começa no 1 e separe até o número que você quer que vá,
nesse caso foi utilizado 10, signicando que ele vai até o último número menor ao 10.

for variavel in range(1,10):
    print(variavel)

'''

'''
* 3 etapas: ínicio, parada e qual é o passo(step - de quanto em quanto você quer que ele pule), 
for variavel in range(1, 12, 3):
    print(variavel)
'''

'''
* Para não se repertir linha por linha, podemos utilizar uma estrutura de repetição
nota1 = float(input('Informe sua nota 1: '))
nota2 = float(input('Informe sua nota 1: '))
nota3 = float(input('Informe sua nota 1: '))
'''

# i é o nome da variável
# onde tem 0 (1, 4) dentro de pode-se colocar tambám assim: (3) - mas vai começar pelo 0.

'''
Existe uma forma de se trabalhar com string, que é chamada de f string, que é
quando você tiver uma string e colocar um f antes das aspas, estará indicando que você quer injetar
uma variavel dentro dela, abrindo chaves {}
'''

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua Nota {i}: '))
    
    soma = soma + nota

print(soma / 3)
