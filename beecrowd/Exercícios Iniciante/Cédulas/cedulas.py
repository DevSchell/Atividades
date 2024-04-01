#ISSO EU NÃO RESOLVI MAS DEIXEI AQUI PARA ESTUDAR A RESOLUÇÃO

# Função para determinar a quantidade mínima de cédulas necessárias
def quantidade_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]  # Lista das cédulas disponíveis
    qtd_cedulas = [0] * len(cedulas)  # Inicializa uma lista para armazenar a quantidade de cada cédula

    # Loop para determinar a quantidade de cada cédula
    for i in range(len(cedulas)):
        qtd_cedulas[i] = valor // cedulas[i]  # Divide o valor pelo valor da cédula para encontrar a quantidade
        valor %= cedulas[i]  # Atualiza o valor restante após a divisão

    # Imprime o resultado
    print(valor)
    for i in range(len(cedulas)):
        print(qtd_cedulas[i], "nota(s) de R$", cedulas[i], ",00")

# Lê o valor da entrada
valor = int(input())

# Chama a função para determinar a quantidade mínima de cédulas
quantidade_cedulas(valor)