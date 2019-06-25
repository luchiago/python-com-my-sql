file = open("sequence.fasta", 'r')
for l in file.readlines():
	if l[0] == ">":
		chave = l[1:].strip()
	else:
		valor = l.strip()

d = {chave : valor}
print(d)