class Carro:

    id_carro = 0

    def __init__(self, consumo, quantidade):
        self.consumo = int(consumo)
        self.quantidade = float(quantidade)
        Carro.id_carro += 1

    def andar(self, dist):
        capacidadeKm = self.consumo * self.quantidade
        qntConsumida = dist / self.consumo
        if qntConsumida > self.quantidade:
            print("O carro não conseguiu fazer todo o trajeto \n"
                  "%.3f Litros no Tanque - %.3f necessarios \n"
                  "O carro andou %.2f km" % (self.quantidade, qntConsumida, capacidadeKm))
            print("______________________________________________________________")
            self.quantidade = 0
        else:
            self.quantidade = self.quantidade - qntConsumida
            print("O carro andou %.2f km \n"
                  "O consumo foi de %.3f Litros" % (dist, qntConsumida))
            print("______________________________________________________________")

    def abastecer(self, qnt):
        self.quantidade = self.quantidade + qnt