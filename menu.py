from gerenciamentoVeiculos import GerenciamentoVeiculos
from gerenciamentoMotoristas import GerenciamentoMotoristas
from gerenciamentoViagem import GerenciamentoViagem
from registrarAbastecimento import RegistrarAbastecimento
from registrarManutencao import RegistrarManutencao

opcoesMenu = None

while (opcoesMenu != 0):
    print('--------------------------')
    print('\n1 - Gerenciamento de Motoristas\n2 - Gerenciamento de Veiculos\n3 - Gerenciamento de Viagem\n4 - Registrar Abastecimento\n5 - Registro de Manutencao\n6 - Relatorio\n0 - Sair')
    print('--------------------------')
    opcoesMenu = int(input('Digite o numero da opcao que deseja fazer: '))

    menuFuncao = None

    if (opcoesMenu == 1):
        while (menuFuncao != 0):
            print('--------------------------')
            print('\n1 - Cadastrar Novo Motorista\n2 - Pesquisar Motorista\n3 - Editar Motorista\n4 - Deletar Motorista\n0 - Voltar ao Menu Principal')
            print('--------------------------')
            menuFuncao = int(input('Digite o numero da opcão que deseja fazer: '))


            if (menuFuncao == 1):
                nome = input('Nome do Motorista: ')
                cpf = input('CPF: ')
                rg = input('RG: ')
                cnh = input('CNH: ')

                motorista = GerenciamentoMotoristas(nome, cpf, rg, cnh)
                motorista.cadastrarMotorista(nome, cpf, rg, cnh)

            elif (menuFuncao == 2):
                cpf = input('CPF do Motorista que deseja PESQUISAR: ')

                motorista.pesquisarMotorista(cpf)

            if (menuFuncao == 3):
                cpf = input('CPF do Motorista que deseja EDITAR: ')

                motorista.editarMotorista(cpf)

            if (menuFuncao == 4):
                cpf = input('CPF do Motorista que deseja DELETAR: ')

                motorista.deletarMotorista(cpf)

    elif (opcoesMenu == 2):
        while (menuFuncao != 0):
            print('--------------------------')
            print('\n1 - Cadastrar Veiculo\n2 - Pesquisar Veiculo\n3 - Editar Veiculo\n4 - Deletar Veiculo\n5 - Quilometragem do Veiculo\n0 - Voltar ao Menu Principal')
            print('--------------------------')
            menuFuncao = int(input('Digite o numero da opcão que deseja fazer: '))

            if (menuFuncao == 1):
                marca = input('Marca do Veiculo: ')
                modelo = input('Modelo do Veiculo: ')
                ano = input('Ano do Veiculo: ')
                placa = input('Placa do Veiculo: ')
                numChassi = input('Numero de chassi do Veiculo: ')
                cor = input('Cor do Veiculo: ')
                quilometragem = input('Quilometragem do Veiculo: ')

                veiculo = GerenciamentoVeiculos(marca, modelo, ano, placa, numChassi, cor, quilometragem)
                veiculo.cadastrarVeiculo(marca, modelo, ano, placa, numChassi, cor, quilometragem)

            elif (menuFuncao == 2):
                placa = input('placa do veiculo que deseja PESQUISAR: ')

                veiculo.editarVeiculo(placa)

            elif (menuFuncao == 3):
                placa = input('placa do veiculo que deseja EDITAR: ')

                veiculo.editarVeiculo(placa)

            elif (menuFuncao == 4):
                placa = input('placa do veiculo que deseja DELETAR: ')

                veiculo.deletarVeiculo(placa)

            elif (menuFuncao == 5):
                placa = input('placa do veiculo que deseja ver a QUILOMETRAGEM: ')

    elif (opcoesMenu == 3):
        while (menuFuncao != 0):
            print('--------------------------')
            print('\n1 - Cadastrar Viagem\n2 - Editar Viagem\n0 - Voltar ao Menu Principal')
            print('--------------------------')
            menuFuncao = int(input('Digite o numero da opcão que deseja fazer: '))
            
            if (menuFuncao == 1):
                destino = input('DESTINO da viagem: ')
                origem = input('ORIGEM da viagem: ')
                distancia = input('DISTANCIA da viagem: ')

                motoristaViagem = input('CPF do motorista que realizou a viagem: ')
                motorista.pesquisarMotorista(motoristaViagem)

                veiculoViagem = input('VEICULO que realizou a viagem: ')
                veiculo.pesquisarVeiculo(veiculoViagem)

                viagem = GerenciamentoViagem(destino, origem, distancia, motoristaViagem, veiculoViagem)
                viagem.cadastrarViagem(destino, origem, distancia, motoristaViagem, veiculoViagem)

            elif (menuFuncao == 2):
                destino = input('DESTINO: ')
                origem = input('ORIGEM: ')
                
                viagem.editarViagem(destino, origem)

    elif (opcoesMenu == 4):
        data = input('Data de abastecimento: ')
        qtdCombustivel = input('Quantidade de Combustivel: ')
        valor = input('Valor do Combustivel: ')

        veiculoAbastecido = input('PLACA do Veiculo: ')
        veiculo.pesquisarVeiculo(veiculoAbastecido)

        abastecimento = RegistrarAbastecimento(veiculoAbastecido, data, qtdCombustivel, valor)
        abastecimento.registrarVeiculosAbastecidos(veiculoAbastecido, data, qtdCombustivel, valor)

    elif (opcoesMenu == 5):
        data = input('Data de Manutencao: ')
        tipoManutencao = input('Tipo de Manutencao: ')
        valor = input('Valor da Manutencao: ')
        
        veiculoManutencao = input('Veiculo: ')
        veiculo.pesquisarVeiculo(veiculoManutencao)

        manutencao = RegistrarManutencao(veiculoManutencao, data, tipoManutencao, valor)
        manutencao.registrarVeiculosMatutencao(veiculoManutencao, data, tipoManutencao, valor)

