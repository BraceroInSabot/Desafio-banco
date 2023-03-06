from datetime import datetime
from typing import NoReturn
from colorama import Fore, Style
from time import sleep
import outros.usuario as usuario, outros.conta as conta, outros.deposito as deposito, outros.saque as saque


"""
def funcionamento(saldo: float, limite_saque: int=0, extrato: dict={}) -> NoReturn:

    while True:
        print(f"\nValor em conta: {saldo}")
        print(f"Limite de saques diários: {limite_saque}/3")
        try:
            operacao: int = int(input("\nDigite o número da operação desejada. \n"))# input
        except ValueError as err:
            print(Fore.RED + f"Houve um erro: {err}" + Style.RESET_ALL)

        if operacao == 1:
            

        elif operacao == 2:
            
        
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
"""


def main():
    extratos: list = []

    while True:
        menu = str(
            input(
                Fore.YELLOW
                + """
            Digite os comandos para realizar as ações:

            [1 ou saque] - Realizar saque
            [2 ou deposito] - Realizar depósito
            [3 ou extrato] - Expor extrato
            [4 ou info] - Retorna informações do usuário logado
            [5 ou usuario] - Cria um novo usuario
            [6 ou conta] - Crie uma nova conta (válido apenas para usuarios cadastrados)

            [SAIR] - Sair do sistema

        """
                + Style.RESET_ALL
            )
        )

        if menu == "1":
            saque.saque()
            extratos.append(saque.dados)
            saque.dados.clear()
        elif menu == "2":
            deposito.deposito()
            extratos.append(deposito.dados)
            deposito.dados.clear()
        elif menu == "3":
            for extrato in extratos:
                if extrato["operacao"] == "saque":
                    print(
                        Fore.CYAN
                        + f"""
                                {extrato["operacao"].upper()}

                        VALOR: R$ {extrato["quantia"]}
                        FEITO EM: {extrato["horario_feito"]}

                        ID: {extrato["id"]}

                        ======================================
                    """
                        + Style.RESET_ALL
                    )
                else:
                    print(
                        Fore.CYAN
                        + f"""
                                {extrato["operacao"].upper()}

                        VALOR: R$ {extrato["quantia"]}
                        FEITO EM: {extrato["horario_feito"]}

                        ID: {extrato["id"]}

                        ======================================
                        """
                        + Style.RESET_ALL
                    )
            sleep(5)
        elif menu == "4":
            usuario.listar_usuario()
        elif menu == "5":
            usuario.criar_usuario()
        elif menu == "6":
            conta.criar_conta()
        elif menu == "SAIR":
            return exit
        else:
            print("Comando inválido, por favor tente novamente.")


if __name__ == "__main__":
    main()
