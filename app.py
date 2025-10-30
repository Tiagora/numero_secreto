import os

restaurantes = [{'nome':'Praça','categoria': 'japonesa','ativo':False},
                {'nome':'Pizza Supreme','categoria': 'italiana','ativo':True},
                {'nome':'Cantina','categoria': 'Mexicana','ativo':False}]

def voltar_ao_menu_principal():
    input(f'Digite a tecla enter para voltar ao menu principal\n')
    main()

def limpar_tela():
    os.system('cls')

def exibir_subtitulo(texto):
    limpar_tela()
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    limpar_tela()
    print('1-Cadastrar restaurante')
    print('2-Listar restaurante')
    print('3-AtivarAlternar estado do restaurante')
    print('4-Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def opcao_invalida(opcao):
    print(f'Opção invalida. Valor: {opcao}, não atende as opções.\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite no nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante{nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante}, foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Lista de restaurantes cadastrados\n')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust (20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        entrada=input('Escolha uma opção: ')
        opcao_escolhida = int(entrada)
    except ValueError:
        opcao_invalida(entrada)

        return
    #print(f'Voce escolheu a opção: {opcao_escolhida}')

    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurante()
    elif opcao_escolhida == 3:
        alternar_estado_restaurante()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
       opcao_invalida(opcao_escolhida)

def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()