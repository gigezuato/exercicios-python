print('=' * 30)
print('Inventário'.center(30))
print('=' * 30)
inventario = {}
while True:
    try:
        print('[ 1- Adicionar novos produtos, 2 - Consultar preços, 3 - Listar todos os produtos e seus valores,'
              ' 4 - Sair]: ')
        opc = int(input('O que deseja fazer? '))
    except ValueError:
        print("Erro! Digite um número inteiro correspondente as opções.")
        opc = 'none'
    match opc:
        case 1:
            print('=== Cadastro Produtos ===')
            produto = str(input('Nome do produto: ')).strip().capitalize()
            valor = float(input('Preço: R$ '))
            inventario[produto] = valor
            print("Item adicionado com sucesso!")
        case 2:
            print('=== Consulta ===')
            if inventario == {}:
                print('Não foram adicionados produtos ainda! Inventário vazio.')
            else:
                nome_produto = str(input('Digite o nome do produto a ser consultado: ')).strip().capitalize()
                for p, v in inventario.items():
                    if p == nome_produto:
                        print(f'{p} ---- R$ {v:.2f}')
        case 3:
            print('=== Produtos ===')
            if inventario == {}:
                print('Não foram adicionados produtos ainda! Inventário vazio.')
            else:
                print('PRODUTOS'.ljust(25, '-'), 'PREÇOS')
                for p, v in inventario.items():
                    print(f'{p.ljust(25, '-')} R$ {v:.2f}')
        case 4:
            print('=== Programa finalizado! ===')
            break
        case _:
            print('Opção inválida!')