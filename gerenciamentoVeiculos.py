class GerenciamentoVeiculos:
    def __init__(self, marca, modelo, ano, placa, numChassi, cor, quilometragem) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.numChassi = numChassi
        self.cor = cor
        self.quilometragem = quilometragem
        self.veiculosCadastrados = list()
      
    def cadastrarVeiculo(self, marca, modelo, ano, placa, numChassi, cor, quilometragem):
        self.veiculosCadastrados.append(GerenciamentoVeiculos(marca, modelo, ano, placa, numChassi, cor, quilometragem))
        print('VEICULO CADASTRADO COM SUCESSO')

    def pesquisarVeiculo(self, placa):
        for busca in self.veiculosCadastrados:
            if busca.placa == placa:
                print('VEICULO ENCONTRADO')
                return busca

           
            print('VEICULO NÃO ENCONTRADO')
            placa = input('Digite a PLACA do veiculo novamente: ')
            self.pesquisarVeiculo(placa)

    def editarVeiculo(self, placa):
        for busca in self.veiculosCadastrados:
            if busca.placa == placa:
                print('VEICULO ENCONTRADO')
                
                print('\n1 - Nova PLACA\n2 - Nova COR\n0 - Sair')
                opcoesEditar = int(
                    input('Digite o numero da opcão que deseja fazer: '))

                if (opcoesEditar == 1):
                    print('Placa antiga: ', busca.placa)
                    novaPlaca = input('Nova placa: ')
                    busca.placa = novaPlaca
                    print('Placa atual: ', busca.placa)
                    return busca

                elif (opcoesEditar == 2):
                    print('Cor antiga: ', busca.cor)
                    novaCor = input('Nova cor: ')
                    busca.cor = novaCor
                    print('Cor atual: ', busca.cor)
                    return busca

            print('VEICULO NÃO ENCONTRADO')

    def deletarVeiculo(self, placa):
        for busca in self.veiculosCadastrados:
            if busca.placa == placa:
                print('VEICULO ENCONTRADO')

                print('\n1 - Deletar Motorista \n0 - Sair')
                opcoesDeletarVeiculo = int(input('Digite o numero da opcão que deseja fazer: '))

                if (opcoesDeletarVeiculo == 1):
                    self.veiculosCadastrados.remove(busca)

                    print('Veiculo removido')
                    return busca
            print('VEICULO NÃO ENCONTRADO')
        