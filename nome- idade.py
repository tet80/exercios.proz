def calcular_dias_de_vida(idade):
    return idade * 365


def main():
    nome = input(("digite sua idade: "))
    try:
        idade = int(input("digite sua idade:  "))
        dias_vividos = calcular_dias_de_vida(idade)
        print(f"ola {nome}, voce ja viveu aproximadamente {dias_vividos} dias.")
    except ValueError:
        print("Por favor, digite uma idade valida (numero inteiro).")

        # main()
