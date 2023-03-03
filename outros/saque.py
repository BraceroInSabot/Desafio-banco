import usuario
from conta import filtrar_conta, contas
from colorama import Fore, Style
from datetime import datetime
from uuid import uuid4

dados = dict()


def saque():
    data = datetime.now()
    id = str(uuid4().int)[0:10]
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
                print(
                    Fore.RED
                    + """
                            Conta não encontrada no sistema!
                        """
                    + Style.RESET_ALL
                )

            valor: float = float(input("\nValor que deseja sacar: "))
        except ValueError as err:
            print(
                Fore.RED
                + f"""
                Houve um erro: {err}
            """
                + Style.RESET_ALL
            )

        for conta in contas:
            if conta["numero_conta"] == numero_conta:
                if conta["limite_saque"] >= 3:
                    print(
                        Fore.RED
                        + """
                            Já foram realizados os 3 saques diários.
                        """
                        + Style.RESET_ALL
                    )
                    return False

                if valor > 500:
                    print(
                        Fore.RED
                        + """
                            Você só pode transferir até 500 reais.
                            """
                        + Style.RESET_ALL
                    )
                    return False

                saldo = conta["saldo"]
                print(saldo)
                if saldo - valor < 0:
                    print(
                        Fore.RED
                        + """
                        Saldo insuficiente.
                        """
                        + Style.RESET_ALL
                    )
                    return False
                else:
                    operacao_dados = {
                        "id_saque": id,
                        "horario_feito": f"{data}",
                        "tipo_acao": "saque",
                        "quantia": valor,
                    }
                    dados.update(operacao_dados)

                    saldo -= valor
                    conta["limite_saque"] += 1
                    # extrato[f"{datetime.now()}"] = ["saque", valor, limite_saque]
                    print(
                        Fore.GREEN
                        + f"""
                        Sacando R$ {valor}...

                        HORARIO: {data}
                        ID DA TRANSIÇÃO: {id}
                        """
                        + Style.RESET_ALL
                    )
                    print("\n" + dados)


saque()
