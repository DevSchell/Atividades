#ENTRADAS
A = round(float(input()),1)
B = round(float(input()),1)
C = round(float(input()),1)

#PROCESSOS
pesoA = 2
pesoB = 3
pesoC = 5
MEDIA = ((A*pesoA)+(B*pesoB)+(C*pesoC))/(pesoA+pesoB+pesoC)

#SAÍDAS
print("MEDIA =", "{:.1f}" .format(MEDIA))