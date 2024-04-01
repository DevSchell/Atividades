#ENTRADAS
a, b, c = map(float, input().split())

#PROCESSOS
maior1 = ((a+b+ abs((a-b))))/2
maiortotal = ((maior1+c+ abs((maior1-c))))/2

#SAÍDAS
print("{:.0f}" .format(maiortotal), "eh o maior")