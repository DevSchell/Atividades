#ENTRADAS
numFunc = int(input())
horaTrab = int(input())
valHora = round(float(input()),2)

#PROCESSOS
salario = horaTrab*valHora

#SAÍDAS
print("NUMBER =", numFunc)
print("SALARY = U$", "{:.2f}".format(salario))