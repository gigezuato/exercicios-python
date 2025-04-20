from funcionalidades.cadastros import *
from funcionalidades.interface import *
from funcionalidades.analises import *

titulo('MINI CADASTRO', '-*', 30)
usuarios = []
while True:
    subtitulo('MENU', ' ', 25)
    linha_horizontal('-', 30)
    print(f'Opções: 1 - Adicionar usuário, 2 - Usuários cadastrados, 3 - Buscar usuário,\n '
          f'4 - Remover ou atualizar usuário, 5 - Analisar dados, 6 - Sair')
    try:
        opc = int(input('O que deseja fazer: '))
        if opc not in range(1, 7):
            opc = 'none'
    except ValueError:
        print('Erro! Por favor, digite um número inteiro!')
        opc = 'none'
    else:
        match opc:
            case 1:
                subtitulo('CADASTRO', '-', 25)
                cadastro(usuarios)
            case 2:
                subtitulo('USUÁRIOS CADASTRADOS', '-', 25)
                mostrar_cadastros(usuarios)
            case 3:
                subtitulo('BUSCA', '-', 25)
                buscar_usuario(usuarios)
            case 4:
                subtitulo('REMOVER OU ATUALIZAR', '-', 25)
                if usuarios == []:
                    print('Não há cadastros ainda!')
                else:
                    while True:
                        try:
                            opc2 = int(input('Deseja 1 - Remover, 2 - Atualizar, 3 - Voltar: '))
                        except ValueError:
                            print('Erro! Digite um número inteiro')
                            opc = 4
                        else:
                            if opc2 not in range(1, 4):
                                print('Opção inválida!')
                                opc2 = 3
                            else:
                                match opc2:
                                    case 1:
                                        subtitulo('REMOVER USUÁRIO', '-', 25)
                                        remover_usuario(usuarios)
                                    case 2:
                                        subtitulo('ATUALIZAR DADOS', '-', 25)
                                        atualizar_dados(usuarios)
                                    case 3:
                                        break
            case 5:
                subtitulo('ANÁLISE DOS DADOS', '-', 25)
                idades = array_idade(usuarios)
                cidades = set_cidade(usuarios)
                analise_idades(idades)
            case 6:
                break
            case _:
                print('Opção inválida!')

linha_horizontal('-*', 30)
print('PROGRAMA FINALIZADO!')