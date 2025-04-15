def saudacao(nome, idade, cidade):
    print(f'Olá {nome.title()}, atualmente você tem {idade} anos e mora na cidade {cidade.capitalize()}!')


n = str(input('Digite seu nome: '))
i = int(input('Digite sua idade: '))
c = str(input('Digite a cidade onde mora: '))
saudacao(n, i, c)