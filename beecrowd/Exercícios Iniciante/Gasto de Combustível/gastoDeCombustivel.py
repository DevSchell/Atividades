#ENTRADAS
tempoViagem = int(input())
velocidadeMedia = int(input())
consumoMedio = 12

#PROCESSOS
distancia = velocidadeMedia*tempoViagem
gasto = distancia/consumoMedio

#SAÍDAS
print("{:.3f}" .format(gasto))