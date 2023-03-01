from datetime import datetime
from typing import NoReturn
from colorama import Fore, Style


def funcionamento(saldo: float, limite_saque: int=0, extrato: dict={}) -> NoReturn:
    """
    Processa o saque e deposito de dinheiro. Para cada ação, armazena dados sobre ela, que é possível ver expondo o extrato.
    """
    print(Fore.YELLOW + """
        Comandos para realizar as ações:
        1 - Realizar saque
        2 - Realizar depósito
        3 - Expor extrato
        4 - Sair do sistema
    """ + Style.RESET_ALL)
    while True:
        print(f"\nValor em conta: {saldo}")
        print(f"Limite de saques diários: {limite_saque}/3")
        operacao: int = int(input("\nDigite o número da operação desejada. \n"))# input

        if operacao == 1:
            if limite_saque >= 3:
                print(Fore.RED + "\nJá foram realizados os 3 saques diários." + Style.RESET_ALL)
                continue

            valor: float = float(input("\nValor que deseja sacar: \n")) # input

            if valor > 500:
                print(Fore.RED + "\nVocê só pode transferir até 500 reais." + Style.RESET_ALL)
                continue
            elif saldo - valor < 0:
                print(Fore.RED + "\nSaldo insuficiente." + Style.RESET_ALL)
                continue
            else:
                saldo -= valor
                limite_saque += 1
                extrato[f"{datetime.now()}"] = ["saque", valor, limite_saque]
                print(Fore.GREEN + f"\nSacando R$ {valor}..." + Style.RESET_ALL)

        elif operacao == 2:
            valor: float = float(input("\nValor que deseja depositar: \n")) # input

            if valor <= 0:
                print(Fore.RED + "\nValor inválido." + Style.RESET_ALL)
                continue
            else:
                saldo += valor
                extrato[f"{datetime.now()}"] = ["deposito", valor]
                print(Fore.GREEN + f"\nFoi depositado o valor de R$ {valor} em sua conta..." + Style.RESET_ALL)
                continue
        
        elif operacao == 3:
            for date, ctx in extrato.items():
                if ctx[0] == "saque":
                    print(Fore.YELLOW + f"\nOperação de SAQUE\nVALOR: {ctx[1]}\nLIMITE DE SAQUE NA HORA: {ctx[2]-1}/3\nREALIZADA EM: {date}\n" + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + f"\nOperação de DEPÓSITO\nVALOR: {ctx[1]}\nREALIZADA EM: {date}\n" + Style.RESET_ALL)
            
        elif operacao == 4:
            print(Fore.GREEN + f"\nVocê está saindo do sistema!".upper() + Style.RESET_ALL)
            return exit()
            
        
        else:
            print(Fore.RED + "Opção Inválida. Tente novamente." + Style.RESET_ALL)
            continue

if __name__ == "__main__":
    saldo = 100
    limite_saque = 0
    extrato = {}
    
    funcionamento(saldo=saldo)