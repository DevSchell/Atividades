#ENTRADAS
A = round(float(input()),1)
B = round(float(input()),1)

#PROCESSOS
pesoA = 3.5
pesoB = 7.5
MEDIA = ((A*pesoA)+(B*pesoB))/(pesoA+pesoB)

#SAÍDA
print("MEDIA =", "{:.5f}".format(MEDIA))
