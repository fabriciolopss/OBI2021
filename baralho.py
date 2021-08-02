

baralho = input()
cartas = list(baralho)
contador = 0
baralhoCartaC = []
baralhoCartaE = []
baralhoCartaU = []
baralhoCartaP = []
C = 13
E = 13
U = 13
P = 13
tamanhobaralho = int(len(baralho)/ 3)
for x in range(tamanhobaralho):
    carta = cartas[contador] + cartas[contador + 1] + cartas[contador + 2]
    if cartas[contador + 2] == 'C':
        C -= 1
        baralhoCartaC.append(carta)
    elif cartas[contador + 2] == 'E':
        E -= 1
        baralhoCartaE.append(carta)
    elif cartas[contador + 2] == 'U':
        U -= 1
        baralhoCartaU.append(carta)
    elif cartas[contador + 2] == 'P':
        P -= 1
        baralhoCartaP.append(carta)
    contador += 3

if (len(baralhoCartaC) != len(set(baralhoCartaC))):
    C = 'erro'
if (len(baralhoCartaE) != len(set(baralhoCartaE))):
    E = 'erro'
if (len(baralhoCartaU) != len(set(baralhoCartaU))):
    U = 'erro'
if (len(baralhoCartaP) != len(set(baralhoCartaP))):
    P = 'erro'
print(C)
print(E)
print(U)
print(P)
