from gerenciamentoMotoristas import GerenciamentoMotoristas
from gerenciamentoVeiculos import GerenciamentoVeiculos

class GerenciamentoViagem:
    def __init__(self, destino, origem, distancia, motorista, veiculo) -> None:
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo
        self.viagensMarcadas = list()

    def cadastrarViagem(self, destino, origem, distancia, motorista, veiculo):               
        self.viagensMarcadas.append(GerenciamentoViagem(destino, origem, distancia, motorista, veiculo))
        print('VIAGEM CADASTRADA COM SUCESSO')

    def editarViagem(self, destino, origem):
        for busca in self.viagensMarcadas:
            if busca.destino == destino and busca.origem == origem:
                print('VIAGEM ENCONTRADO')
                
                
                print('\n1 - Novo Destino\n2 - Nova Origem\n3 - Nova Distancia\n4 - Novo Motorista\n5 - Novo Veiculo\n0 - Sair')
                opcoesEditar = input('Digite o numero da opcão que deseja fazer: ')

                if (opcoesEditar == 1):
                    print('Destino Atual: ', busca.destino)
                    novoDestino = input('Novo Destino: ')
                    busca.destino = novoDestino
                    print('Destino Atualizado: ', busca.destino)
                    return busca
                
                elif (opcoesEditar == 2):
                    print('Origem Atual: ', busca.origem)
                    novaOrigem = input('Nova Origem: ')
                    busca.origem = novaOrigem
                    print('Origem Atualizada: ', busca.origem)
                    return busca
                
                elif (opcoesEditar == 3):
                    print('Distancia Atual: ', busca.distancia)
                    novaDistancia = input('Novo Destino: ')
                    busca.distancia = novaDistancia
                    print('Distancia Atualizada: ', busca.distancia)
                    return busca
                
                elif (opcoesEditar == 4):                
                    print('Motorista Atual: ', busca.motorista)
                    novoMotorista = input('Novo Motorista: ')
                    busca.motorista = novoMotorista
                    print('Motorista Atualizado: ', busca.motorista)
                    return busca
                
                elif (opcoesEditar == 5):
                    print('Veiculo Atual: ', busca.veiculo)
                    novoVeiculo = input('Novo Veiculo: ')
                    busca.veiculo = novoVeiculo
                    print('Veiculo Atualizado: ', busca.veiculo)
                    return busca
            
            print('VIAGEM NÃO ENCONTRADA')