import datetime
import os

menu = """

***********************************
*                                 *
*         [d] Depositar           *
*         [s] Sacar               *
*         [e] Extrato             *
*         [l] Limpar Tela         *
*         [q] Sair                *
*                                 *
***********************************
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

mensagem = ""

while True:
    os.system("cls")
    
    data = datetime.date.today()
    hoje = ("00" + str(data.day))[-2:] + "/" + ("00" + str(data.month))[-2:] + "/" + str(data.year)

    print(menu)
    print(mensagem)
    opcao = input("Informe a opção: ").lower()

    if opcao == "d":
        
        valor = input("\nInforme o valor do depósito: ")
        valor = float(valor) if len(valor) > 0 else 0

        if valor > 0:
            saldo += valor
            
            extrato += hoje + " - "
            extrato += f"Depósito de R$ {valor:.2f}\n"
            
            print ("\n+----------")
            print(f"|  Depósito de R$ {valor:.2f} realizado com sucesso!")
            print(f"|  Seu saldo atual é de R$ {saldo:.2f}")
            print ("+----------")

        else:
            print("\n=> Operação falhou! O valor informado é inválido.")


        mensagem = ""
        input("")


    elif opcao == "s":

        print(f"\n=> Seu saldo atual é de R$ {saldo:.2f}\n")

        if saldo > 0:
            valor = input("Informe o valor do saque: ")
            valor = float(valor) if len(valor) > 0 else 0
     
            excedeu_saldo = valor > saldo 
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("\n=> Operação falhou! Você não tem saldo suficiente.")
            
            elif excedeu_limite:
                print("\n=> Operação falhou! O valor do saque excedeu o limite.")
            
            elif excedeu_saques:
                print("\n=> Operação falhou! Número máximo de saques excedido.")
            
            elif valor > 0:
                saldo -= valor
                extrato += hoje + " - "
                extrato += f"Saque de R$ {valor:.2f}\n"
                numero_saques += 1
                
                print ("\n+----------")
                print(f"|  Saque de R$ {valor:.2f} realizado com sucesso!")
                print(f"|  Seu saldo atual é de R$ {saldo:.2f}")
                print ("+----------")
                

            else:  
                print("Operação falhou! O valor informado é inválido.")
            

            mensagem = ""
            input("")


        else:  
            mensagem = """
+---------------------------------+
|  Você não tem saldo suficiente  |
|  para saque.                    |
+---------------------------------+
"""


    elif opcao == "e":
        print("\n===================== EXTRATO =====================\n")
        print("=> Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===================================================")

        mensagem = ""
        input("")


    elif opcao == "l":
        mensagem = ""
        continue


    elif opcao == "q":
        break


    else:
        mensagem = """
+-------------------------------------------------------+
|  Operação inválida!                                   |
|  Por favor, selecione novamente a operação desejada.  |
+-------------------------------------------------------+
"""
