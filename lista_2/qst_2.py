nome = input("Digite o nome do arquivo: ")
file = open(nome, 'r')
print(file.read())
file.close()