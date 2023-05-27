idade_cibele = int(input('Cibele, Qual a sua idade?'))
idade_fernanda = int(input('Fernada, Qual a sua idade?'))
idade_celeste = int(input('Celeste, Qual a sua idade?'))

if 5 <= idade_cibele <= 100 and 5 <= idade_fernanda <= 100 and 5 <= idade_celeste <= 100:
    if idade_cibele < idade_fernanda and idade_fernanda < idade_celeste:
        idade_final = idade_fernanda
    elif idade_cibele < idade_celeste and idade_celeste < idade_fernanda:
        idade_final = idade_celeste
    else:
        idade_final = idade_cibele

    print(idade_final)
