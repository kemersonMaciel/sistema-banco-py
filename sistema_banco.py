menu = """

[1] Depositar 
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ { valor: .2f}\n"

        else: 
            print("Operação não realizada! O Valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Opreção não realizada! Seu saldo não é suficiente.")
        
        elif excedeu_limite:
            print("Opreção não realizada! Seu limite não é suficiente.")

        elif excedeu_saques:
            print("Opreção não realizada! Excedeu limite de saque diário")

        elif valor > 0:
            saldo -= valor
            extrato += f" Valor Saque: R$ {valor: .2f}\n"
            numero_saques += 1

    
        else:
            print ("Operação não realizada! Valor informado não é válido")

    elif opcao == "3":
        print("\n ================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo: .2f}")
        print("============================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida. Por favor, selecione operação correta.")