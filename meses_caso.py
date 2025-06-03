print("DIGITE O NÚMERO CORRESPONDENTE AO MÊS:")
print("""1 - JANEIRO 2 - FEVEREIRO 3 - MARÇO 4 - ABRIL 5 - MAIO 6 - JUNHO 
7 - JULHO 8 - AGOSTO 9 - SETEMBRO 10 - OUTUBRO 11 - NOVEMBRO 12 - DEZEMBRO""")

meses = {
    1: "JANEIRO", 2: "FEVEREIRO", 3: "MARÇO", 4: "ABRIL", 5: "MAIO", 6: "JUNHO",
    7: "JULHO", 8: "AGOSTO", 9: "SETEMBRO", 10: "OUTUBRO", 11: "NOVEMBRO", 12: "DEZEMBRO"
}

try:
    numero = int(input("Sua escolha: "))
    mes = meses.get(numero, "MÊS INVÁLIDO")
except ValueError:
    mes = "ENTRADA INVÁLIDA. Digite um número inteiro."

print("O mês selecionado é:", mes)
