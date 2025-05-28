# Solicita ao usuário o salário bruto
salario_bruto = float(input("Digite o salário bruto: R$ "))

# Calcula o desconto do INSS
if salario_bruto <= 1518.00:
    inss = salario_bruto * 0.075
elif salario_bruto <= 2793.88:
    inss = salario_bruto * 0.09 - 22.77
elif salario_bruto <= 4190.83:
    inss = salario_bruto * 0.12 - 106.59
elif salario_bruto <= 8157.41:
    inss = salario_bruto * 0.14 - 190.40
else:
    inss = 951.62  # Teto de contribuição para salários acima de R$ 8.157,41

# Calcula a base de cálculo para o IR
base_ir = salario_bruto - inss

# Calcula o desconto do IR
if base_ir <= 2259.20:
    ir = 0
elif base_ir <= 2826.65:
    ir = base_ir * 0.075 - 169.44
elif base_ir <= 3751.05:
    ir = base_ir * 0.15 - 381.44
elif base_ir <= 4664.68:
    ir = base_ir * 0.225 - 662.77
else:
    ir = base_ir * 0.275 - 896.00

# Calcula o salário líquido
salario_liquido = salario_bruto - inss - ir

# Exibe o resultado
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IR: R$ {ir:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
