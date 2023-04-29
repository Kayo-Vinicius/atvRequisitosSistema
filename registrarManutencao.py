class RegistrarManutencao:
    def __init__(self, veiculo, data, tipoManutencao, custo) -> None:
        self.veiculo = veiculo
        self.data = data
        self.tipoManutencao = tipoManutencao
        self.custo = custo
        self.veiculosManutencao = list()

    def registrarVeiculosMatutencao(self, veiculo, data, tipoManutencao, custo):
        self.veiculosManutencao.append(RegistrarManutencao(veiculo, data, tipoManutencao, custo))
        print('MANUTENCAO REGISTRADA COM SUCESSO')
        