import math as m

a = float(input("Digite o 'a' da equação: "))
b = float(input("Digite o 'b' da equação: "))
c = float(input("Digite o 'c' da equação: "))

delta = b**2 - 4*a*c
x1 = (-b + m.sqrt(delta))/2*a
x2 = (-b - m.sqrt(delta))/2*a
print(x1, x2)