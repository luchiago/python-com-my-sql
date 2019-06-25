def arquivo(choice):
	try:
		file = open('teste.txt', 'r')
	except:
		print("\nFalha na Leitura\n")
		return
	if choice == 2:
		print("\n" + file.read() + "\n")
	else:
		print("\nLeitura feita\n")

if __name__ == '__main__':
	while True:
		print("O que deseja fazer?")
		print("1 - Leitura de arquivo")
		print("2 - Impressão")
		print("3 - Sair")
		choice = int(input(">"))
		if choice == 3:
			print("Tchau")
			break
		if choice == 1 or choice == 2:
			arquivo(choice)