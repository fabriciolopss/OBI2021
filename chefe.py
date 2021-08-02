totalNum = int(input())
numeros = []
soma = 0
chefeNum = 0
for x in range(totalNum):
    ordenador = x
    loopIson = True
    chefeNum = int(input())
    numeros.append(chefeNum)
    if (x > 1):
        while (loopIson):
            if chefeNum == 0:
                if numeros[ordenador - 1] != 0:
                    numeros[ordenador - 1] = 0
                    loopIson = False
                else:
                    ordenador -= 1
            else:
                loopIson = False
    elif (x == 1):
        if chefeNum == 0:
            numeros[x - 1] = 0
    if x == totalNum:
        for y in range(len(numeros)):
            soma += int(numeros[y])


print(soma)
