#ENTRADAS
vend = input()
salario = float(input())
vendas = float(input())

#PROCESSOS
comissao = (vendas*0.15)
total = salario+comissao

#SAÍDAS
print("TOTAL = R$","{:.2f}".format(total))