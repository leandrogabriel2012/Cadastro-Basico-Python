from dao.dao_pessoa import DAOPessoa
from model.pessoa import Pessoa

# Classe que gera ação de dependendo da seleção na classe MenuTerminal
class Opcao():

    # Construtor só gera título da opção
    def __init__(self, mensagem = 'Opção Inválida!'):
        print(mensagem)

    # Inserir Cadastro
    # Cadastro deve ter string com pelo menos 1 caractere para cada campo
    def inserir(self):
        nome = input('Nome: ')
        registro = input('Registro: ')
        nascimento = input('Data Nascimento: ')

        if self.__valor_valido(nome) and self.__valor_valido(registro) and self.__valor_valido(nascimento):
            dao = DAOPessoa(Pessoa(registro, nome, nascimento))
            dao.inserir()
            print('Inserido com sucesso!')
        else:
            print('Cadastro não inserido!')

    # Excluir cadastro baseado no campo registro
    def excluir(self):
        registro = input('Registro: ')
        dao = DAOPessoa(Pessoa(registro))
        if dao.excluir():
            print('Cadastro Excluído!')
        else:
            print('Registro Não Encontrado!')

    # Busca registro digito
    # Primeiro seleciona Registro
    #   > Mostra cadastro com número do registro (Caso exista)
    #   > Caso seja bem-sucedido, é confirmado
    def alterar(self):
        registro = input('Registro: ')
        dao = DAOPessoa(Pessoa(registro))

        linha = dao.buscar()
        if linha:
            print(linha)

            nome = input('Nome: ')
            nascimento = input('Nascimento: ')
            dao = DAOPessoa(Pessoa(registro))
            dao.alterar(Pessoa(registro, nome, nascimento))

            linha = dao.buscar()
            if linha:
                print(linha)
                print('Cadastro alterado!')
            else:
                print('Erro ao Apresentar Registro!')

        else:
            print('Cadastro Não Encontrado')

    # Lista todos os campos no arquivo "dados.csv"
    def listar(self):
        DAOPessoa.listar()

    # Busca Cadastro pelo nome no Registro
    def buscar_por_nome(self):
        nome = input('Digite o Nome: ')
        if nome != '':
            linha = DAOPessoa.buscar_por_nome(nome)
            if linha:
                print(linha.replace(',', ' | '))
            else:
                print('Nome Não Encontrado!')
        else:
            print('Nome Inválido!')

    # Campos só são válidos se tiver pelo menos um caractere
    def __valor_valido(self, valor):
        if valor != '':
            return True
        else:
            return False