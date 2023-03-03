from uuid import uuid4
from colorama import Fore, Style
from time import sleep

usuarios = [
    {
        "id": "15632",
        "nome": "Guilherme",
        "cpf": "123",
        "data_de_nascimento": "12062003",
        "endereço": "Rua tal",
        "saldo": 100,
    },
    {
        "cpf": "456",
        "id": "963",
    },
]

"""
    {
        "cpf": "123",
        "id": "852",
    },
    {
        "cpf": "456",
        "id": "963",
    },
"""


def listar_usuario():
    """
    Procura por um usuario através do CPF
    """
    id = str(
        input("\nDigite o ID do usuario cadastrado para retornar as suas informações: ")
    )
    usuario = [usuario for usuario in usuarios if usuario["id"] == id]

    return print(
        Fore.GREEN
        + f"""
        ID: {usuario[0]["id"]}
        NOME: {usuario[0]["nome"]}
        CPF: {usuario[0]["cpf"]}
        DATA DE NASCIMENTO: {usuario[0]["data_de_nascimento"]}
        ENDEREÇO: {usuario[0]["endereço"]}
    """
        + Style.RESET_ALL
    )


def filtrar_usuario(cpf, id):
    """
    Filtrar por CPF e por ID
    """
    if [usuario for usuario in usuarios if usuario["cpf"] == cpf]:
        return True
    elif [usuario for usuario in usuarios if usuario["id"] == id]:
        return True
    else:
        return False


def criar_usuario():
    """CPF, Nome, Data de nascimento, Endereço"""
    while True:
        cpf = str(input("\nInsira o seu CPF: "))

        if filtrar_usuario(cpf=cpf, id=None):
            print("\nUsuário já cadastrado no banco de dados!")
            return

        nome = str(input("\nInsira o seu nome: "))
        nascimento = str(input("\nInsira a sua data de nascimento: "))
        endereco = str(input("\nInforme o local da sua residência (Cidade/Estado): "))

        while True:
            random_id = str(uuid4().int)[0:5]

            if not filtrar_usuario(cpf=None, id=random_id):
                break

        conta = {
            "id": random_id,
            "nome": nome,
            "cpf": cpf,
            "data_de_nascimento": nascimento,
            "endereço": endereco,
        }

        usuarios.append(conta)
        print(
            Fore.GREEN
            + """
            Usuário foi criado com sucesso!
        """
            + Style.RESET_ALL
        )
        print(
            Fore.GREEN
            + f"""
        ID: {conta["id"]}
        NOME: {conta["nome"]}
        CPF: {conta["cpf"]}
        DATA DE NASCIMENTO: {conta["data_de_nascimento"]}
        ENDEREÇO: {conta["endereço"]}
    """
            + Style.RESET_ALL
        )
        sleep(3)
        return usuarios


listar_usuario()
