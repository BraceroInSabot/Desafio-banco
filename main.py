from objetos.usuario import Usuario
from objetos.sistema_conta.sistema_historico.historico import Historico
from time import sleep
from colorama import Fore
from colorama import Style


def main():
    MENSAGEM_BOAS_VINDAS = """
    BEM VINDO, CLIENTE A INTERFACE DO BANCO (X)

    Para poder operar no nosso banco, crie um usuário!
    """

    MENSAGEM_NAVEGACAO = """
    MENU DE NAVEGAÇÃO

    [1] - SACAR
    [2] - DEPOSITAR
    [3] - INFORMAÇÕES DO USUÁRIO
    [4] - INFORMAÇÕES DA CONTA
    [5] - VER EXTRATOS

    """

    print(MENSAGEM_BOAS_VINDAS)
    sleep(3)

    while True:
        try:
            usuario_logado = Usuario().criar_usuario()
        except (ValueError, TypeError) as err:
            print(err)

        if usuario_logado:
            break

    while True:
        try:
            user_op = int(input(MENSAGEM_NAVEGACAO))
        except ValueError as err:
            print(
                Fore.RED
                + "\nSão válidos apenas números inteiros nesta seção."
                + Style.RESET_ALL
            )

        if user_op == 1:
            try:
                valor = float(input("\nDigite um valor para realizar o saque: "))
            except ValueError as err:
                print(Fore.RED + "\nValor inválido." + Style.RESET_ALL)
                continue
            usuario_logado[1].saque(valor)
        elif user_op == 2:
            try:
                valor = float(input("\nDigite um valor para reazliar o depósito: "))
            except ValueError as err:
                print(Fore.RED + "\nValor inválido." + Style.RESET_ALL)
                continue
            usuario_logado[1].deposito(valor)
        elif user_op == 3:
            print(usuario_logado[0].info_usuario)
        elif user_op == 4:
            print(usuario_logado[1].info_conta)
        elif user_op == 5:
            print(Historico().ver_extratos())

            # print(usuario_logado[0].info_usuario)
            # usuario_logado = Usuario().criar_usuario()
            # print(usuario_logado[0].info_usuario)


if __name__ == "__main__":
    main()
