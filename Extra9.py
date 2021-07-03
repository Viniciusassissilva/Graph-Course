class Funcionario:

    id_funcionario = 0

    def __init__(self, nome, salario):
        self.nome = str(nome)
        self.salario = float(salario)
        Funcionario.id_funcionario += 1