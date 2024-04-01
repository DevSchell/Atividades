# ENTRADAS
item1cod, item1qtd, item1val = map(float, input().split())
item2cod, item2qtd, item2val = map(float, input().split())

# PROCESSOS
total = (item1qtd * item1val) + (item2qtd * item2val)

# SAÍDAS
print("VALOR A PAGAR: R$", "{:.2f}".format(total))
