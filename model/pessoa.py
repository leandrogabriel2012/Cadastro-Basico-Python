from model.model import Model

# Model para cadastro Pessoa (Encapsular o tipo Pessoa)
# Único Model utilizado no sistema
# Possui pouco campos apenas para construção de sistema
class Pessoa(Model):

    def __init__(self, registo, nome='', nascimento=''):
        self.__nome = nome
        self.__registro = registo
        self.__nascimento = nascimento

    def __str__(self):
        return f'Nome: {self.__nome} \t | \t Registro: {self.__registro} \t | \t Nascimento: {self.__nascimento}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, registro):
        self.__registro = registro

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento
