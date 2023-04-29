class RegistrarAbastecimento:
    def __init__(self, veiculo, data, qtdCombustivel, valor) -> None:
        self.veiculo = veiculo
        self.data = data
        self.qtdCombustivel = qtdCombustivel
        self.valor = valor
        self.veiculosAbastecidos = list()

    def registrarVeiculosAbastecidos(self, veiculo, data, qtdCombustivel, valor):
        self.veiculosAbastecidos.append(RegistrarAbastecimento(veiculo, data, qtdCombustivel, valor))
        print('ABASTECIMENTO REGISTRADO COM SUCESSO')
        