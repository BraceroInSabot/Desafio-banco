from usuario import filtrar_usuario, usuarios
from colorama import Style, Fore
from uuid import uuid4
from typing import NoReturn

contas = []


def criar_conta() -> NoReturn:
    while True:
        cpf = str(input("Válide o seu CPF: "))

        if not filtrar_usuario(cpf=cpf, id=None):
            print("Usuário não cadastrado! Volte e faça o cadastro.")
            return

        usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        random_id = str(uuid4().int)[0:12]
        conta = {
            "agencia": "0001",
            "numero_conta": random_id,
            "usuario": usuario_filtrado,
        }
        contas.append(conta)

        print(
            Fore.GREEN
            + """
            Conta criada com sucesso!
            """
            + Style.RESET_ALL
        )
        print(
            Fore.GREEN
            + f"""
            Agência: {conta["agencia"]}
            Número da conta: {conta["numero_conta"]}

            Nome do dono da conta: {conta["usuario"][0]["nome"]}
        """
            + Style.RESET_ALL
        )
        return
