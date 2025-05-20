from datetime import datetime

def calcular_dias_de_vida(nome, data_nascimento):
    # Obtém a data atual
    hoje = datetime.now()
    
    # Calcula a diferença entre a data atual e a data de nascimento
    dias_vividos = (hoje - data_nascimento).days
    
    # Retorna o nome e a quantidade de dias vividos
    return nome, dias_vividos

def main():
    # Solicita o nome do usuário
    nome = input("Digite seu nome: ")
    
    # Solicita a data de nascimento do usuário no formato DD/MM/AAAA
    data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    
    try:
        # Converte a string para um objeto datetime
        data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")
        
        # Chama a função para calcular os dias de vida
        nome, dias_vividos = calcular_dias_de_vida(nome, data_nascimento)
        
        # Exibe o resultado
        print(f"\n{nome}, você viveu aproximadamente {dias_vividos} dias.")
    
    except ValueError:
        print("⚠️ Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")

if __name__ == "__main__":
    main()
