def menu():
    menu_text = """\n
    =========== MENU ===========
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [5]\tNova conta
    [6]\tListar contas
    [7]\tNovo usuario
    [4] Sair
    ==============================
    """
    return input(menu_text)

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("\n Operacao falhou! O valor informado e invalido. ")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n peracao falhou! Voce nao tem saldo suficiente.")

    elif excedeu_limite:
        print("\n Operacao falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\n Operacao falhou! Numero maximo de saques excedido. ")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n Operacao falhou! O valor informado e invalido. ")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nao foram realizadas movimentacoes." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Ja existe usuario com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuario criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n suario nao encontrado, fluxo de criacao de conta encerrado! ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "7":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "4":
            break

        else:
            print("Operacao invalida, por favor selecione novamente a operacao desejada.")

if __name__ == "__main__":
    main()
