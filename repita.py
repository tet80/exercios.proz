opcao = -1
while True:
    print("-------------")
    print("1 - Digite olá!")
    print("2 - Dizer oi!")
    print("0 - Sair do programa")
    print("---------------")
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue  # Retorna ao início do loop sem executar o restante do código
    
    if opcao == 1:
        print("olá!")
    elif opcao == 2:
        print("Oi!")
    elif opcao == 0:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
