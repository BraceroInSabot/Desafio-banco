from colorama import Fore
from colorama import Style


class Historico:
    extratos = []

    def __init__(self, extratos=extratos) -> None:
        self.__extratos = extratos

    def adicionar_transacao(self, operacao_dados):
        self.extratos.append(operacao_dados)

    def ver_extratos(self):
        for extrato in self.extratos:
            MENSAGEM_VER_EXTRATO = f"""
            TIPO DE OPERAÇÃO: {extrato["operacao"].upper()}
            VALOR DA OPERAÇÃO: R$ {extrato["valor_depositado"]}
            ID DA OPERAÇÃO: {extrato["id_operacao"]}
            """
            print(Fore.YELLOW + MENSAGEM_VER_EXTRATO + Style.RESET_ALL)
