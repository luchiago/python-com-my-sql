seq = input()
texto = ">kdmer\n" + seq
filename = "sequence2.fasta"
file = open(filename, 'w')
file.write(texto)
file.close()