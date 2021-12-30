from menu.menu import Menu
from menu.opcao import Opcao

# Classe que gera Opção baseado no menu selecionado
# Função start() chama menu, cada opção gera uma ação da classe Opcao()
class MenuTerminal(Menu):

    def __imprime_titulo_menu(self):  # Chama o Título do Menu
        texto_menu = '| [I]nserir | [E]xcluir | [A]lterar | [L]istar | [B]uscar | [S]air |'
        cumprimento = len(texto_menu)
        print('─' * cumprimento); print(texto_menu); print('̅' * cumprimento)

    def start(self): # Chama Menu

        while True: # Sempre gerará Menu enquanto não selecionar para Sair

            self.__imprime_titulo_menu()
            opcao = input('Selecione a opção: ')
            opcao = opcao.upper()
            print('\n')

            if opcao == 'I': # Switch para opções
                Opcao('Insira Pessoa: ').inserir()
            elif opcao == 'E':
                Opcao('Selecione Registro: ').excluir()
            elif opcao == 'A':
                Opcao('Selecione Registro: ').alterar()
            elif opcao == 'L':
                Opcao('Lista de Cadastrados: ').listar()
            elif opcao == 'B':
                Opcao('Buscar por Nome: ').buscar_por_nome()
            elif opcao == 'S':
                Opcao('Fim de Sistema!')
                break
            else:
                Opcao()