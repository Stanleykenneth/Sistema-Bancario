saldo = 500.0
opcao = -1

def depositar():
    valor = float(input("Informe o valor que deseja depositar: \n"))
    return valor

def sacar():
    valor = float(input("Informe o valor que desja sacar: \n"))
    return valor

print()
print("""          SEJA BEM VINDO """)

while opcao != 0:
    opcao = int(input( """

          
     ESCOLHA A OPÇÃO DESEJADA      
    ========== MENU ==========

    1 - DEPOSITAR
    2 - SACAR
    3 - SALDO
    0 - SAIR

    ==========================
    """))

    if opcao == 1: 
        valor_deposito = depositar()
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito} realizado com sucesso.")
        continue
    elif opcao == 2:
        valor_saque = float(input("Digite o valor que deseja sacer: \n"))
        if valor_saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor_saque    
        print(f"Saque de R$ {valor_saque} realizado com sucesso.")
        continue
    elif opcao == 3:
        print(f" Seu saldo atual é  de R$ {saldo}")
        continue
    elif opcao == 0:
        print("Obrigado por usar nosso Sistema!")
        SystemExit()
    else:
        print("Opção inválida!")
        


