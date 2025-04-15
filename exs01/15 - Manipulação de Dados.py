inventario = {}


def adicionar_produtos(produtos, codigo, nome, preco):
    produtos.update({codigo: {'Produto': nome, 'Preço': preco}})
    print(f'Item {nom} adicionado!')


def atualizar_preco(produtos, codigo, novo_preco):
    try:
        produtos[codigo]['Preço'] = novo_preco
    except KeyError:
        print(f'Erro! O código {codigo} não existe!')
    else:
        print('Preço atualizado!')


def buscar_produto(produtos, codigo):
    try:
        print(f'{produtos[codigo]['Produto']} = {produtos[codigo]['Preço']:.2f}')
    except KeyError:
        print(f'Erro! O código {codigo} não existe!')


def remover_produto(produtos, codigo):
    try:
        resp = str(input(f'Deseja realmente remover o item {produtos[codigo]['Produto']}? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            print(f'Item {produtos[codigo]['Produto']} removido!')
            del produtos[codigo]
        else:
            print('Operação cancelada!')
    except KeyError:
        print(f'Erro! O código {codigo} não existe!')


print('=' * 30)
print('Inventário'.center(30))
print('=' * 30)
while True:
    try:
        print('1 - Adicionar produtos, 2 - Atualizar preço, 3 - Buscar produto, 4 - Remover produto, 5 - Sair')
        opc = int(input('O que deseja fazer? '))
    except ValueError:
        print('Erro! Digite um valor inteiro!')
        opc = 'none'
    match opc:
        case 1:
            print('=== CADASTRO DE PRODUTOS ===')
            cod = str(input('Código: '))
            nom = str(input('Nome: ')).capitalize().strip()
            valor = float(input('Preço: R$ '))
            adicionar_produtos(inventario, cod, nom, valor)
        case 2:
            print('=== ATUALIZAÇÃO DE PREÇOS ===')
            if inventario == {}:
                print('Não há produtos cadastrados!')
            else:
                cod = str(input('Digite o código do produto: '))
                novo_valor = float(input('Novo preço: R$ '))
                atualizar_preco(inventario, cod, novo_valor)
        case 3:
            print('=== CONSULTA DE PRODUTOS ===')
            if inventario == {}:
                print('Não há produtos cadastrados!')
            else:
                cod = str(input('Digite o código do produto: '))
                buscar_produto(inventario, cod)
        case 4:
            print('=== REMOVER PRODUTOS ===')
            if inventario == {}:
                print('Não há produtos cadastrados!')
            else:
                cod = str(input('Digite o código do produto: '))
                remover_produto(inventario, cod)
        case 5:
            print('---- Programa encerrado! ----')
            break
        case _:
            print('Opção inválida!')