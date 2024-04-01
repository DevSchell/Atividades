#ENTRADAS
a, b, c = map(float, input().split())

#PROCESSOS
areaTriRet = (a*c)/2
areaCirculo = 3.14159*(c**2)
areaTrapezio = ((a+b)*c)/2
areaQuadrado = b**2
areaRetangulo = a*b

#SAÍDAS
print("TRIANGULO:", "{:.3f}".format(areaTriRet))
print("CIRCULO:","{:.3f}".format( areaCirculo))
print("TRAPEZIO:", "{:.3f}".format( areaTrapezio))
print("QUADRADO:","{:.3f}".format( areaQuadrado))
print("RETANGULO:", "{:.3f}".format( areaRetangulo))