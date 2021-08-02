pessoas = [None] * 100
armazenado = []
interacoes = int(input())

def strip(msg):
    initalizer = list(msg)
    if (initalizer[0] == 'R'):
        num = int(msg.strip("R "))
        armazenado.append(num)
        pessoas[num] = 0

    elif(initalizer[0] == 'E'):
        num = int(msg.strip("E "))
        for x in range(len(armazenado)):
            pessoas[armazenado[x]] += 1
            if armazenado[x] == num:
                pessoas[armazenado[x]] -= 1


    elif(initalizer[0] == 'T'):
        num = int(msg.strip("T "))
        for x in range (len(armazenado)):
            pessoas[armazenado[x]] += num
for x in range(interacoes):
    msg = input()
    strip(msg)

for x in range (len(armazenado)):
    print("{} {}".format(armazenado[x],pessoas[armazenado[x]]))

