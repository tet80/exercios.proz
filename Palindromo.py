numero = input("Digite um número inteiro para verificar se é um palídromo")

if numero == numero[:: 1]:
    print (f"o número {numero} é um palídromo ")
    
else:
    print(f"o número {numero} não é um palídromo")
    