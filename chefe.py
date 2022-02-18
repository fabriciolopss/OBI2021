#Meu Gabarito para OBI 2021
#Estou refazendo a prova para treinar para OBI de 2022
#Adotei alguns conceitos que aprendi durante esse ano

class numeros():
    def __init__(self):
        self.quantNumeros = 0
        self.numeros = []
        self.somaTotal = 0

    def inputDados(self, quant):
        self.quantNumeros = quant
        for x in range(self.quantNumeros):
            numLista = int(input())
            if numLista != 0:
                self.numeros.append(numLista)
            else:
                del self.numeros[len(self.numeros) - 1]
        self.somarNumeros()
        return self.somaTotal

    def somarNumeros(self):
        for y in self.numeros:
            self.somaTotal += y

prova = numeros()
print (prova.inputDados(int(input())))
