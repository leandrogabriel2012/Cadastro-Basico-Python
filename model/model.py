from abc import ABC, abstractmethod

# Apenas para padronizar classes Model para possível outros tipos de cadastro
class Model(ABC):

    @abstractmethod
    def __init__(self):
        pass