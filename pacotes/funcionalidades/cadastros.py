from funcionalidades.interface import *


def cadastro(dados):
    while True:
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        email = str(input('Email: ')).strip()
        cidade = str(input('Cidade: ')).strip().title()
        profissao = str(input('Profissão: ')).strip().title()

        usuario = {'Nome': nome,
                   'Idade': idade,
                   'Email': email,
                   'Cidade': cidade,
                   'Profissão': profissao
                   }
        dados.append(usuario)
        print('Cadastro realizado com sucesso!')
        while True:
            resp = str(input('Deseja fazer mais cadastros? [S/N]: ')).strip().upper()[0]
            if resp not in 'SN':
                print('Opção inválida!')
            else:
                break
        if resp == 'N':
            break


def mostrar_cadastros(dados):
    if dados == []:
        print('Não há cadastros ainda!')
    else:
        for i in range(len(dados)):
            print(f'{i+1} - {dados[i].get('Nome')}')


def buscar_usuario(dados):
    while True:
        if dados == []:
            print('Não há cadastros ainda!')
            break
        else:
            usuario = str(input('Nome do usuário: ')).upper().title()
            linha_horizontal('*', 20)
            for i, user in enumerate(dados):
                if user['Nome'] == usuario:
                    for k, v in user.items():
                        print(f'{k}: {v}')
                    break
            else:
                print(f'Não há registros do usuário {usuario}. Faça o cadastro!')
            linha_horizontal('*', 20)
        while True:
            resp = str(input('Deseja fazer mais buscas? [S/N]: ')).strip().upper()[0]
            if resp not in 'SN':
                print('Opção inválida!')
            else:
                break
        if resp == 'N':
            break


def remover_usuario(dados):
    usuario = str(input('Nome do usuário que irá remover: ')).strip().title()
    while True:
        confirma = str(input(f'Tem certeza que quer remover o usuário {usuario}? [S/N]: ')).strip().upper()[0]
        if confirma not in 'SN':
            print('Opção inválida!')
        elif confirma == 'S':
            for i, user in enumerate(dados):
                if user['Nome'] == usuario:
                    del dados[i]
                    print('Usuário deletado!')
                    break
            else:
                print(f'O usuário {usuario} não existe!')
            break
        else:
            break


def atualizar_dados(dados):
    usuario = str(input('Nome do usuário: '))
    for i, user in enumerate(dados):
        if user['Nome'] == usuario:
            subtitulo('Dados atuais', '*', 20)
            for k, v in user.items():
                print(f'{k}: {v}')
            linha_horizontal('*', 20)
            break
    else:
        print('Esse usuário não existe!')
        return
    print('-> Atualize os dados: ')
    for i, user in enumerate(dados):
        if user['Nome'] == usuario:
            user.update({'Nome': str(input('Nome: ')).strip().title()})
            user.update({'Idade': int(input('Idade: '))})
            user.update({'Email': str(input('Email: ')).strip()})
            user.update({'Cidade': str(input('Cidade: ')).strip().title()})
            user.update({'Profissão': str(input('Profissão: ')).strip().title()})
    print('Dados atualizados com sucesso!')