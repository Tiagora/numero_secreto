import textwrap

# ================= CPF =================
def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10) % 11
    dig1 = 0 if dig1 == 10 else dig1

    if dig1 != int(cpf[9]):
        return False

    # Segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10) % 11
    dig2 = 0 if dig2 == 10 else dig2

    return dig2 == int(cpf[10])

# ================= MENU =================
def menu():
    return input(textwrap.dedent("""
    ========== MENU ==========
    [d]\tDepositar
    [s]\tSacar
    [t]\tTransferir
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """))

# ================= USUÁRIO =================
def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u['cpf'] == cpf), None)

def criar_usuario(usuarios):
    cpf = input("CPF: ")

    if not validar_cpf(cpf):
        print("CPF inválido!")
        return

    if filtrar_usuario(cpf, usuarios):
        print("Usuário já existe!")
        return

    nome = input("Nome: ")
    nascimento = input("Data nascimento: ")
    endereco = input("Endereço: ")

    usuarios.append({
        "nome": nome,
        "cpf": ''.join(filter(str.isdigit, cpf)),
        "nascimento": nascimento,
        "endereco": endereco
    })

    print("Usuário criado!")

# ================= CONTAS =================
def filtrar_conta(numero, contas):
    return next((c for c in contas if c['numero_conta'] == numero), None)

def criar_conta(agencia, numero, usuarios, contas):
    cpf = input("CPF do usuário: ")
    cpf = ''.join(filter(str.isdigit, cpf))

    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado!")
        return

    conta = {
        "agencia": agencia,
        "numero_conta": numero,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "saques": 0
    }

    contas.append(conta)
    print("Conta criada!")

# ================= OPERAÇÕES =================
def depositar(conta):
    valor = float(input("Valor: "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        print("Ok")
    else:
        print("Valor inválido")

def sacar(conta, limite=500, limite_saques=3):
    valor = float(input("Valor: "))

    if valor > conta['saldo']:
        print("Saldo insuficiente")
    elif valor > limite:
        print("Excede limite")
    elif conta['saques'] >= limite_saques:
        print("Limite de saques atingido")
    elif valor > 0:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
        conta['saques'] += 1
        print("Ok")
    else:
        print("Valor inválido")

def transferir(contas):
    origem_num = int(input("Conta origem: "))
    destino_num = int(input("Conta destino: "))
    valor = float(input("Valor: "))

    origem = filtrar_conta(origem_num, contas)
    destino = filtrar_conta(destino_num, contas)

    if not origem or not destino:
        print("Conta inválida")
        return

    if origem['saldo'] < valor:
        print("Saldo insuficiente")
        return

    origem['saldo'] -= valor
    destino['saldo'] += valor

    origem['extrato'] += f"Transferência enviada: R$ {valor:.2f}\n"
    destino['extrato'] += f"Transferência recebida: R$ {valor:.2f}\n"

    print("Transferência realizada!")

# ================= EXTRATO =================
def exibir_extrato(conta):
    print("\n=== EXTRATO ===")
    print(conta['extrato'] or "Sem movimentação")
    print(f"Saldo: R$ {conta['saldo']:.2f}")

# ================= LISTAGEM =================
def listar_contas(contas):
    for c in contas:
        print(f"Agência: {c['agencia']} | Conta: {c['numero_conta']} | Titular: {c['usuario']['nome']}")

# ================= MAIN =================
def main():
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        op = menu()

        if op == 'nu':
            criar_usuario(usuarios)

        elif op == 'nc':
            numero = len(contas) + 1
            criar_conta(AGENCIA, numero, usuarios, contas)

        elif op in ['d', 's', 'e']:
            numero = int(input("Conta: "))
            conta = filtrar_conta(numero, contas)

            if not conta:
                print("Conta não encontrada")
                continue

            if op == 'd':
                depositar(conta)
            elif op == 's':
                sacar(conta)
            else:
                exibir_extrato(conta)

        elif op == 't':
            transferir(contas)

        elif op == 'lc':
            listar_contas(contas)

        elif op == 'q':
            break

        else:
            print("Opção inválida")

main()

'''
import textwrap

def menu():
    menu = """\n
    ==========MENU========= 
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado, por favor cadastro o usuário antes de criar a conta. @@@")
        return

    print("\n=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))  
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
                    
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1  
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta) 
                numero_conta += 1   

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.") 


main()
'''