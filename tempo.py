
#Realizando atividade tempo.py da OBI de 2021 para treinar para proxima

class Tempo():
    def __init__(self):
        self.tempoAcumulado = 0
        self.contatos = {}
        self.contatosAtivos = []
        self.numInputs = 0
        self.numAtual = 0

    def somarTempo(self):
        for x in self.contatosAtivos:
            if (x == self.numAtual):
                pass
            else:
                self.contatos[x] += 1

    def mensagensSemResposta(self):
        try:
            for x in self.contatosAtivos:
                self.contatos[x] = -1
        except: 
            pass

    def calcularTempo(self, stringCompleta):
        tipo, numAmigo = stringCompleta.split(' ')
        if (tipo == 'R'):
            self.numAtual = numAmigo
            self.contatosAtivos.append(numAmigo)
            if numAmigo in self.contatos:
                pass
            else:
                self.contatos[numAmigo] = 0 
            self.somarTempo()
        elif(tipo == 'T'):
            for x in self.contatosAtivos:
                self.contatos[x] += (int(numAmigo) - 1)
        elif(tipo == "E"):
            self.numAtual = numAmigo
            self.contatos[numAmigo] += 1
            self.contatosAtivos.remove(numAmigo)
            self.somarTempo()
            
    def mainLoop(self, num):
        self.numInputs = num
        for x in range(self.numInputs):
            self.calcularTempo(input())
        self.mensagensSemResposta()
        for amigo, tempo in self.contatos.items():
            print("{} {}".format(amigo, tempo))

programa = Tempo()
programa.mainLoop(int(input())) 