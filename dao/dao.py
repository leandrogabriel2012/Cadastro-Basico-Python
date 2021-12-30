from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def inserir(self):
        pass

    @abstractmethod
    def excluir(self):
        pass

    @abstractmethod
    def alterar(self):
        pass

    @staticmethod
    def listar():
        pass

    @abstractmethod
    def buscar(self):
        pass