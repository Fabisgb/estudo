# > ESTRUTURAS CONDICIONAIS


'''
Este código está comentado, pois introduzimoa abaixo outro código para teste,
pois daria conflito

idade = 20

# if significa se

# pode se pensar nos dois pontos como sendo então
if idade >= 18:
    print ('Você é maior de Idade.')

# pode se pensar em else como: Do contrário então
else:
    print ('Você é menor de Idade.')

   
* Imagine nque você queira imprimir "Aprovada(o)", caso o estudante tenha uma média
superior ou igual a 7, e "Reprovada(o), caso a média seja inferior a 7.
*


media = float (input('Informe a média do estudante:'))


if media >= 7:
    print ('Você foi Aprovada(o)')

# No python não existe else if, foi incurtado para elif
elif media >= 5:
    print ('Você foi para a Recuperação')
else:
    print ('Você foi Reprovada(o)')
'''

media = 10
presença = 100

#Comparação conjunta pode-se usar o AND ou OR, significando E.
if media >=7 and presença >=7:
    print ('Você foi Aprovada(o)')
else:
    print ('Você foi Reprovada(o)')