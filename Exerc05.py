class Bomba:
    "Uma Bomba, Fire in the hole"
    id_Bomba = 0

    def __init__(self, tipo_Combustivel, valor_Litro, qnt_Combustivel):
        self.tipo_Combustivel = tipo_Combustivel
        self.valor_Litro = valor_Litro
        self.qnt_Combustivel = qnt_Combustivel
        Bomba.id_Bomba += 1

    def abastecer_valor(self, valor):

        litros = valor / self.valor_Litro
        print("Foi adicionado ao combustivel %.2f Litros" % (litros))
        self.qnt_Combustivel += litros
        print(("O tanque possui %.2f combustivel " % (self.qnt_Combustivel)))

    def abastecer_qnt(self, qnt):

        valor = qnt * self.valor_Litro
        print("Foi adicionado ao combustivel R$ %.2f " % (valor))
        self.qnt_Combustivel += qnt
        print(("O tanque possui %.2f  litros de combustivel " % (self.qnt_Combustivel)))


bomba1 = Bomba("Gasolina", 5, 0)

bomba1.abastecer_valor(100)
bomba1.abastecer_qnt(50)