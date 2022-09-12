infile = open("ip-in.txt", "r")
correto = open('ip-correto.txt', 'w')
incorreto = open('errado.txt', 'w')
ip = []
lido = infile.readlines()
infile.close()
for i in lido:
    sep = i.split(".")
    for pulo in sep:
        pulo = pulo.strip("\n")
        ip.append(int(pulo))
    if 256 > ip[0] > 0 and 256 > ip[1] >= 0 and 256 > ip[2] >= 0 and 256 > ip[3] >= 0:
        correto.writelines(i)
    else:
        incorreto.writelines(i)
    ip = []
correto.close()
incorreto.close()
