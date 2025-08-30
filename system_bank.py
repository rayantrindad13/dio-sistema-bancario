menu = '''
    "1": depositar,
    "2": sacar,
    "3": extrato,
    "4": sair
    => '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. Tente novamente.")
        
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("Limite de saque excedido.")
        elif excedeu_saques:
            print("Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print("Valor inválido. Tente novamente.")
        

    elif opcao == "3":
        print("\n=== Extrato ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===============")
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
