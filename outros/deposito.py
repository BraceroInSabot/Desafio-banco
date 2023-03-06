import outros.usuario as usuario

from colorama import Fore, Style
from outros.conta import filtrar_conta, contas
from datetime import datetime
from uuid import uuid4

dados = dict()


def deposito():
    data = datetime.now()
    id_deposito = str(uuid4().int)[0:10]

    while True:
        try:
            cpf: str = str(input("\nInforme o CPF da conta destinada o depósito: "))
            if not usuario.filtrar_usuario(cpf=cpf, id=None):
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
                print(
                    Fore.RED
                    + """
                        Conta não encontrada no sistema!
                    """
                    + Style.RESET_ALL
                )

            valor: float = float(input("\nValor que deseja depositar: "))
        except ValueError as err:
            print(
                Fore.RED
                + f"""
                Houve um erro: {err}
            """
                + Style.RESET_ALL
            )

        if valor <= 0:
            print(
                Fore.RED
                + """
                Valor inválido.
            """
                + Style.RESET_ALL
            )
            continue
        else:
            for conta in contas:
                if conta["numero_conta"] == numero_conta:
                    operacao_deposito: float = conta["saldo"]
                    operacao_deposito += valor
                    conta.update({"saldo": operacao_deposito})

                    operacao_dados = {
                        "id": id_deposito,
                        "horario_feito": data,
                        "tipo_acao": "deposito",
                        "quantia": valor,
                    }
                    dados.update(operacao_dados)

                    print(
                        Fore.GREEN
                        + f"""
                    Foi depositado o valor de R$ {valor} em sua conta.

                    SALDO ATUAL: {conta["saldo"]}
                    HORARIO: {data}
                    ID DA TRANSIÇÃO: {id_deposito}
                    """
                        + Style.RESET_ALL
                    )

            return
