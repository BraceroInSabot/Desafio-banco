from datetime import datetime


def funcionamento(saldo: float, limite_saque: int=3, extrato: dict={}) -> str:
    while True:
        print(f"\nValor em conta: {saldo}")
        print(f"Limite de saques diários: {limite_saque}/3")
        operacao: int = int(input("\nDigite o número da operação desejada. \n"))# input

        if operacao == 1:
            if limite_saque >= 3:
                print("Já foram realizados os 3 saques diários.")
                continue

            valor: float = float(input("\nValor que deseja sacar: \n")) # input

            if valor > 500:
                print("\nVocê só pode transferir até 500 reais.")
                continue
            elif saldo - valor < 0:
                print("\nSaldo insuficiente.")
                continue
            else:
                saldo -= valor
                limite_saque += 1
                extrato[f"{datetime.now()}"] = ["saque", valor, limite_saque]
                print(F"\nSacando R$ {valor}...")

        elif operacao == 2:
            valor: float = float(input("\nValor que deseja depositar: \n")) # input

            if valor <= 0:
                print("\nValor inválido.")
                continue
            else:
                saldo += valor
                extrato[f"{datetime.now()}"] = ["deposito", valor]
                print(f"\nFoi depositado o valor de R$ {valor} em sua conta...")
                continue
            
        elif operacao == 4:
            return "\nVocê está saindo do sistema!".upper()
            break
        
        else:
            print("Opção Inválida. Tente novamente.")


if __name__ == "__main__":
    saldo = 100
    limite_saque = 0
    extrato = {}
    
    funcionamento(saldo=saldo)