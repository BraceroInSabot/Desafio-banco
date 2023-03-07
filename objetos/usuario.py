from uuid import uuid4
from colorama import Fore
from colorama import Style
from .sistema_conta.conta import Conta


class Usuario(Conta):
    id = str(uuid4().int)[0:5]

    def __init__(self, id=id, nome=None, cpf=None, data_nascimento=None, endereco=None):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco

    @property
    def info_usuario(self):
        return (
            Fore.GREEN
            + f"""

            
DADOS DO USUÁRIO

ID: {self.__id}
NOME: {self.__nome}


		"""
            + Style.RESET_ALL
        )

    def criar_usuario(self):
        nome = str(input("Nome: "))
        cpf = str(input("CPF: "))
        data_nascimento = str(input("Data de nascimento: "))
        endereco = str(input("Endereço: "))

        usuario = Usuario(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco=endereco,
        )

        conta = Conta.criar_conta(self, nome=nome, cpf=cpf)
        return [usuario, conta]
