from abc import ABC, abstractmethod

# Superclasse para todos  os Menus
# Apenas para definir padrão dos menus que possam ser gerados
class Menu(ABC):

    @abstractmethod
    def start(self): # Inicialização do Menu
        pass