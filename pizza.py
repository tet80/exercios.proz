

# site de pizzaria
print("PIZZARIA COMA BASTANTE - SEJA BEM VINDO")
print("___ CARDAPIO - PREÇO _____")
print(" ")
print("******* PIZZAS - SABORES ******")
print(" CALABRESA, FRANGO, CATUPIRY")
print("******* PIZZA - TAMANHO *******")
print(" PIZZA PEQUENA  R$ 10,00")
print(" PIZZA MÉDIA   R$ 15,00")
print(" PIZZA GRANDE  R$ 20,00")
print("********* REFRIGERANTE *******")
print(" COCA-COLA     R$ 7,00")
print(" GUARANÁ       R$ 6,00")
print(" FANTA         R$ 5,00")
print("_____________________________")
print(" ")
print("FAÇA O SEU PEDIDO PARA PIZZA")
print("1 - CALABRESA")
print("2 - FRANGO")
print("3 - CATUPIRY")
print("______________________________")

# Lê a escolha do sabor da pizza
pedidopizza = int(input())
print("DIGITE O TAMANHO DA PIZZA:")
print("P - PEQUENA")
print("M - MÉDIA")
print("G - GRANDE")
print("______________________")

# Lê o tamanho da pizza
tampizza = input().upper()

print("FAÇA O SEU PEDIDO PARA REFRIGERANTE:")
print("1 - COCA - COLA")
print("2 - GUARANÁ")
print("3 - FANTA")
print("______________________")

# Lê a escolha do refrigerante
pedidorefri = int(input())

# Calcular o preço e o pedido

# Pedido 1 - CALABRESA
if pedidopizza == 1 and tampizza == "P" and pedidorefri == 1:
    precopagar = 10.00 + 7.00
    pedidos = "CALABRESA, PEQUENA, COCA-COLA"
elif pedidopizza == 1 and tampizza == "P" and pedidorefri == 2:
    precopagar = 10.00 + 6.00
    pedidos = "CALABRESA, PEQUENA, GUARANÁ"
elif pedidopizza == 1 and tampizza == "P" and pedidorefri == 3:
    precopagar = 10.00 + 5.00
    pedidos = "CALABRESA, PEQUENA, FANTA"
    
# Pedido 2 - CALABRESA
elif pedidopizza == 1 and tampizza == "M" and pedidorefri == 1:
    precopagar = 15.00 + 7.00
    pedidos = "CALABRESA, MÉDIA, COCA-COLA"
elif pedidopizza == 1 and tampizza == "M" and pedidorefri == 2:
    precopagar = 15.00 + 6.00
    pedidos = "CALABRESA, MÉDIA, GUARANÁ"
elif pedidopizza == 1 and tampizza == "M" and pedidorefri == 3:
    precopagar = 15.00 + 5.00
    pedidos = "CALABRESA, MÉDIA, FANTA"

# Pedido 3 - CALABRESA
elif pedidopizza == 1 and tampizza == "G" and pedidorefri == 1:
    precopagar = 20.00 + 7.00
    pedidos = "CALABRESA, GRANDE, COCA-COLA"
elif pedidopizza == 1 and tampizza == "G" and pedidorefri == 2:
    precopagar = 20.00 + 6.00
    pedidos = "CALABRESA, GRANDE, GUARANÁ"
elif pedidopizza == 1 and tampizza == "G" and pedidorefri == 3:
    precopagar = 20.00 + 5.00
    pedidos = "CALABRESA, GRANDE, FANTA"

# Pedido 4 - FRANGO
elif pedidopizza == 2 and tampizza == "P" and pedidorefri == 1:
    precopagar = 10.00 + 7.00
    pedidos = "FRANGO, PEQUENA, COCA-COLA"
elif pedidopizza == 2 and tampizza == "P" and pedidorefri == 2:
    precopagar = 10.00 + 6.00
    pedidos = "FRANGO, PEQUENA, GUARANÁ"
elif pedidopizza == 2 and tampizza == "P" and pedidorefri == 3:
    precopagar = 10.00 + 5.00
    pedidos = "FRANGO, PEQUENA, FANTA"

# Pedido 5 - FRANGO
elif pedidopizza == 2 and tampizza == "M" and pedidorefri == 1:
    precopagar = 15.00 + 7.00
    pedidos = "FRANGO, MÉDIA, COCA-COLA"
elif pedidopizza == 2 and tampizza == "M" and pedidorefri == 2:
    precopagar = 15.00 + 6.00
    pedidos = "FRANGO, MÉDIA, GUARANÁ"
elif pedidopizza == 2 and tampizza == "M" and pedidorefri == 3:
    precopagar = 15.00 + 5.00
    pedidos = "FRANGO, MÉDIA, FANTA"

# Pedido 6 - FRANGO
elif pedidopizza == 2 and tampizza == "G" and pedidorefri == 1:
    precopagar = 20.00 + 7.00
    pedidos = "FRANGO, GRANDE, COCA-COLA"
elif pedidopizza == 2 and tampizza == "G" and pedidorefri == 2:
    precopagar = 20.00 + 6.00
    pedidos = "FRANGO, GRANDE, GUARANÁ"
elif pedidopizza == 2 and tampizza == "G" and pedidorefri == 3:
    precopagar = 20.00 + 5.00
    pedidos = "FRANGO, GRANDE, FANTA"

# Pedido 7 - CATUPIRY
elif pedidopizza == 3 and tampizza == "P" and pedidorefri == 1:
    precopagar = 10.00 + 7.00
    pedidos = "CATUPIRY, PEQUENA, COCA-COLA"
elif pedidopizza == 3 and tampizza == "P" and pedidorefri == 2:
    precopagar = 10.00 + 6.00
    pedidos = "CATUPIRY, PEQUENA, GUARANÁ"
elif pedidopizza == 3 and tampizza == "P" and pedidorefri == 3:
    precopagar = 10.00 + 5.00
    pedidos = "CATUPIRY, PEQUENA, FANTA"

# Pedido 8 - CATUPIRY
elif pedidopizza == 3 and tampizza == "M" and pedidorefri == 1:
    precopagar = 15.00 + 7.00
    pedidos = "CATUPIRY, MÉDIA, COCA-COLA"
elif pedidopizza == 3 and tampizza == "M" and pedidorefri == 2:
    precopagar = 15.00 + 6.00
    pedidos = "CATUPIRY, MÉDIA, GUARANÁ"
elif pedidopizza == 3 and tampizza == "M" and pedidorefri == 3:
    precopagar = 15.00 + 5.00
    pedidos = "CATUPIRY, MÉDIA, FANTA"

# Pedido 9 - CATUPIRY
elif pedidopizza == 3 and tampizza == "G" and pedidorefri == 1:
    precopagar = 20.00 + 7.00
    pedidos = "CATUPIRY, GRANDE, COCA-COLA"
elif pedidopizza == 3 and tampizza == "G" and pedidorefri == 2:
    precopagar = 20.00 + 6.00
    pedidos = "CATUPIRY, GRANDE, GUARANÁ"
elif pedidopizza == 3 and tampizza == "G" and pedidorefri == 3:
    precopagar = 20.00 + 5.00
    pedidos = "CATUPIRY, GRANDE, FANTA"

else:
    precopagar = 0.0
    pedidos = "PEDIDO INVÁLIDO"

# Exibir o total
print("_____________________________________")
print(f" O TOTAL A PAGAR É: R$ {precopagar: .2f}")
print("_____________________________________________")
print(f"OS PEDIDOS FORAM {pedidos}")
print("________________________________________")
print("BOM APETITE E SEJA BEM VINDO")