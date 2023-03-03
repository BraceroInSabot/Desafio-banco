from colorama import Fore, Style
from usuario import filtrar_usuario
from conta import filtrar_conta


def deposito():
    while True:
        try:
            cpf: str = str(input("\nInforme o CPF da conta destinada o depósito: "))
            if not filtrar_usuario(cpf=cpf, id=None):
                print(
                    Fore.RED
                    + """
                        Usuário não conta no sistema!
                    """
                    + Style.RESET_ALL
                )

            numero_conta: str = str(
                input("\nInforme o número da conta destinada o depósito: ")
            )
            if not filtrar_conta(cpf=cpf, numero_conta=numero_conta):
                pass

            valor: float = float(input("\nValor que deseja depositar: "))
        except ValueError as err:
            print(Fore.RED + f"Houve um erro: {err}" + Style.RESET_ALL)

        if valor <= 0:
            print(Fore.RED + "\nValor inválido." + Style.RESET_ALL)
            continue
        else:
            saldo += valor
            extrato[f"{datetime.now()}"] = ["deposito", valor]
            print(
                Fore.GREEN
                + f"\nFoi depositado o valor de R$ {valor} em sua conta..."
                + Style.RESET_ALL
            )
            continue
