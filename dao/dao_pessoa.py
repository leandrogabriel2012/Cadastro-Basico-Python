from dao.dao import DAO
import csv

CAMINHO_ARQUIVO = './dados/dados.csv'

class DAOPessoa(DAO):

    def __init__(self, pessoa):
        self.__pessoa = pessoa

    #insere um registro
    def inserir(self):
        with open(CAMINHO_ARQUIVO, 'at', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow([self.__pessoa.nome, self.__pessoa.registro, self.__pessoa.nascimento])

    #excluir registro pelo número de registro
    def excluir(self):
        registro_excluido = False

        with open(CAMINHO_ARQUIVO, mode='r') as arquivo_csv:
            leitor = arquivo_csv.readlines()
            texto = ''

            for linha in leitor:
                item = linha.split(',') #Separar para comparar os registros

                if len(item) > 1:
                    if self.__pessoa.registro != item[1]:
                        texto = texto + linha
                    else:
                        registro_excluido = True

        with open(CAMINHO_ARQUIVO, mode='w') as arquivo_csv:
            arquivo_csv.write(texto)

        return registro_excluido

    #altera nome e data de nascimento pelo número de registro
    def alterar(self, pessoa):
        texto = ''

        with open(CAMINHO_ARQUIVO, mode='tr') as arquivo_csv:
            arquivo = arquivo_csv.readlines()

            for linha in arquivo:
                item = linha.split(',') #Separar para comparar os registros
                if pessoa.registro == item[1]:
                    texto = texto + pessoa.nome + ',' + pessoa.registro + ',' + pessoa.nascimento + '\n'
                else:
                    texto = texto + linha

        with open(CAMINHO_ARQUIVO, mode='tw') as arquivo_csv:
            arquivo_csv.write(texto)

    #lista todos os registros
    @staticmethod
    def listar():
        print('\n')
        with open(CAMINHO_ARQUIVO, mode='r') as arquivo_csv:
            leitor = arquivo_csv.read().replace(',', '\t | \t')
            print(leitor)

    #Buscar registro de self.__registro
    def buscar(self):
        with open(CAMINHO_ARQUIVO, mode='r') as arquivo_csv:
            leitor = arquivo_csv.readlines()

            for linha in leitor:
                item = linha.split(',')

                if len(item) > 1:
                    if self.__pessoa.registro == item[1]:
                        return linha

        return False

    @staticmethod
    def buscar_por_nome(nome):
        with open(CAMINHO_ARQUIVO, mode='r') as arquivo_csv:
            leitor = arquivo_csv.readlines()

            for linha in leitor:
                item = linha.split(',')

                if len(item) > 0:
                    if nome == item[0]:
                        return linha

        return False