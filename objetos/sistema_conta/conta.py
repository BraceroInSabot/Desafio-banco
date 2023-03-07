from uuid import uuid4
from colorama import Fore
from colorama import Style
from .sistema_historico.historico import Historico


class Conta(Historico):
    nro_conta = str(uuid4().int)[0:10]
    id = str(uuid4().int)[0:5]
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    SALDO = 0.0

    def __init__(
        self,
        id=id,
        nome=None,
        cpf=None,
        nro_conta=nro_conta,
        agencia=AGENCIA,
        saldo=SALDO,
        limite_saque=LIMITE_SAQUE,
    ):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__nro_conta = nro_conta
        self.agencia = agencia
        self.__saldo = saldo
        self.__limite_saque = limite_saque

    @property
    def info_conta(self):
        """
        Retorna as informações da conta do usuário
        """
        listar_conta = (
            Fore.GREEN
            + f"""


DADOS DA CONTA

ID {self.__id} - NÚMERO DA CONTA {self.__nro_conta} - AGÊNCIA {self.agencia}

NOME: {self.__nome} 
SALDO EM CONTA: R$ {self.__saldo}


    """
            + Style.RESET_ALL
        )

        return listar_conta

    def deposito(self, valor):
        """
        Realiza a ação de DEPÓSITO para a conta do usuário
        """
        if valor >= 1:
            self.__saldo += valor

            Historico.adicionar_transacao(
                self,
                operacao_dados={
                    "operacao": "deposito",
                    "valor_depositado": valor,
                    "id_operacao": str(uuid4().int)[0:15],
                },
            )

            print(
                Fore.GREEN
                + f"""


FEITO. SEU DEPÓSITO FOI UM SUCESSO!.

SALDO ATUAL: R$ {self.__saldo}
VALOR TRANSFERIDO: R$ {valor}


"""
                + Style.RESET_ALL
            )
            return self.__saldo
        else:
            print(
                Fore.RED
                + "Valor inválido, por favor, digite um número decimal POSITIVO"
                + Style.RESET_ALL
            )
            return False

    def saque(self, valor):
        """
        Realiza a ação de SAQUE para a conta do usuário
        """
        if valor >= 1:
            if not self.__saldo - valor < 0:
                if self.__limite_saque > 0:
                    self.__limite_saque -= 1
                    self.__saldo -= valor
                    print(
                        Fore.GREEN
                        + f"""


Saque de R$ {valor} realizado com sucesso.

SALDO ATUAL: R$ {self.__saldo}
SAQUES DIÁRIOS: restam {self.__limite_saque}/3 unidades


                """
                        + Style.RESET_ALL
                    )
                else:
                    print(
                        Fore.RED + "Limites de saque insuficientes!" + Style.RESET_ALL
                    )
            else:
                print(Fore.RED + "Saldo insuficiente!" + Style.RESET_ALL)
        else:
            print(
                Fore.RED
                + "Valor inválido! por favor, digite um número decimal POSITIVO"
                + Style.RESET_ALL
            )

    def criar_conta(self, nome, cpf):
        """
        Cria uma conta para o usuário
        """
        conta = Conta(
            nome=nome,
            cpf=cpf,
        )

        return conta
