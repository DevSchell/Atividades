#ENTRADAS
distanciakm = float(input())
litrosgastos = float(input())

#PROCESSOS
consumo = distanciakm/litrosgastos

#SAÍDAS
print("{:.3f}".format(consumo), "km/l")