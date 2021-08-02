
placar = 0
resultado = 0
for x in range(6):
    resultado = input()
    if (resultado == 'V'):
        placar += 1

if (placar == 6 or placar == 5):
    print(1)
elif(placar == 3 or placar == 4):
    print(2)
elif(placar == 1 or placar == 2):
    print(3)
elif (placar == 0):
    print(-1)
