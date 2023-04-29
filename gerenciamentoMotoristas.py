
class GerenciamentoMotoristas:
    def __init__(self, nome, cpf, rg, cnh) -> None:
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cnh = cnh
        self.motoristasCadastrados = list()


    def cadastrarMotorista(self, nome, cpf, rg, cnh):
        self.motoristasCadastrados.append(
            GerenciamentoMotoristas(nome, cpf, rg, cnh))

        print('MOTORISTA CADASTRADO COM SUCESSO')

    def pesquisarMotorista(self, cpf):
        for busca in self.motoristasCadastrados:
            if busca.cpf == cpf:
                print('MOTORISTA ENCONTRADO')
                return busca

            print('MOTORISTA NÃO ENCONTRADO')
            cpf = input('Digite o CPF do motorista novamente: ')
            self.pesquisarMotorista(cpf)       

    def editarMotorista(self, cpf):
        for busca in self.motoristasCadastrados:
            if busca.cpf == cpf:
                print('MOTORISTA ENCONTRADO')

                print('\n1 - Novo NOME\n2 - Novo CPF\n3 - Novo RG\n4 - NovA CNH\n0 - Sair')
                opcoesEditar = int(input('Digite o numero da opcão que deseja fazer: '))

                if (opcoesEditar == 1):
                    print('Nome antigo: ', busca.nome)
                    novoNome = input('Novo nome: ')
                    busca.nome = novoNome
                    print('Nome atual: ', busca.nome)
                    return busca

                elif (opcoesEditar == 2):
                    print('CPF antigo: ', busca.cpf)
                    novoCPF = input('Novo CPF: ')
                    busca.cpf = novoCPF
                    print('CPF atual: ', busca.cpf)
                    return busca

                elif (opcoesEditar == 3):
                    print('RG antigo: ', busca.rg)
                    novoRG = input('Novo RG: ')
                    busca.rg = novoRG
                    print('RG atual: ', busca.rg)
                    return busca

                elif (opcoesEditar == 4):
                    print('CNH antiga: ', busca.cnh)
                    novaCNH = input('Nova CNH: ')
                    busca.rg = novaCNH
                    print('CNH atual: ', busca.cnh)
                    return busca

            print('MOTORISTA NÃO ENCONTRADO')

    def deletarMotorista(self, cpf):
        for busca in self.motoristasCadastrados:
            if busca.cpf == cpf:
                print('MOTORISTA ENCONTRADO')

                print('\n1 - Deletar Motorista \n0 - Sair')
                opcoesDeletarMotorista = int(
                    input('Digite o numero da opcão que deseja fazer: '))

                if (opcoesDeletarMotorista == 1):
                    self.motoristasCadastrados.remove(busca)

                    print('Motorista removido')
                    return busca

            print('MOTORISTA NÃO ENCONTRADO')