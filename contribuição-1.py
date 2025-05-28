# Solicita ao usuário o salário de contribuição
salario_contribuicao = float(input("Digite o salário de contribuição: R$ "))

# Inicializa a variável para armazenar o valor da contribuição
contribuicao_inss = 0.0

# Calcula a contribuição conforme as faixas salariais
if salario_contribuicao <= 1518.00:
    contribuicao_inss = salario_contribuicao * 0.075
elif salario_contribuicao <= 2793.88:
    contribuicao_inss = salario_contribuicao * 0.09 - 22.77
elif salario_contribuicao <= 4190.83:
    contribuicao_inss = salario_contribuicao * 0.12 - 106.59
elif salario_contribuicao <= 8157.41:
    contribuicao_inss = salario_contribuicao * 0.14 - 190.40
else:
    contribuicao_inss = 951.62  # Teto de contribuição para salários acima de R$ 8.157,41

# Exibe o valor da contribuição
print(f"O valor da contribuição do INSS é: R$ {contribuicao_inss:.2f}")
ssss