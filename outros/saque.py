import usuario
from conta import filtrar_conta, contas
from colorama import Fore, Style

print(contas[0]["limite_saque"])

while True:
    try:
        cpf: str = str(input("\nInforme o CPF da conta destinada o saque: "))
        if not usuario.filtrar_usuario(cpf=cpf, id=None):
            print(
                Fore.RED
                + """
                    Usuário não conta no sistema!
                """
                + Style.RESET_ALL
            )

        numero_conta: str = str(
            input("\nInforme o número da conta destinada o saque: ")
        )
        if not filtrar_conta(cpf=cpf, numero_conta=numero_conta):
            pass

        valor: float = float(input("\nValor que deseja depositar: "))
    except ValueError as err:
        print(
            Fore.RED
            + f"""
            Houve um erro: {err}
        """
            + Style.RESET_ALL
        )

    if limite_saque >= 3:
        print(Fore.RED + "\nJá foram realizados os 3 saques diários." + Style.RESET_ALL)
        continue

    try:
        valor: float = float(input("\nValor que deseja sacar: \n"))  # input
    except ValueError as err:
        print(Fore.RED + f"Houve um erro: {err}" + Style.RESET_ALL)

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
