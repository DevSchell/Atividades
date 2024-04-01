from math import sqrt
#ENTRADAS
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

#PROCESSOS
dist = sqrt((((x2 - x1)**2) + (y2 - y1)**2))

#SAíDAS
print("{:.4f}" .format(dist))