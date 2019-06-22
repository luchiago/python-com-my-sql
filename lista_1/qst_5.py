entrada = input().split()
n1 = int(entrada[0])
n2 = int(entrada[1])
sinal = entrada[2]

if sinal == '+':
	print(n1 + n2)
elif sinal == '-':
	print(n1 - n2)
elif sinal == '*':
	print(n1 * n2)
elif sinal == '/':
	print(n1 / n2)
else:
	print("Você digitou errado meu camarada")