import pickle

class Contato:
    def __init__(self, nome, telefone, endereco, relacao):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.relacao = relacao

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\nRelação: {self.relacao}"

class Agenda:
    def __init__(self):
        self.contatos = []
        self.ultimo = -1

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if nome.lower() in contato.nome.lower():
                return contato
        return None

    def inserir_alterar_contato(self, nome, telefone, endereco, relacao):
        contato = self.buscar_contato(nome)
        if contato:
            contato.telefone = telefone
            contato.endereco = endereco
            contato.relacao = relacao
            print("Contato atualizado com sucesso!")
        else:
            if len(self.contatos) < 1000:
                novo_contato = Contato(nome, telefone, endereco, relacao)
                self.contatos.append(novo_contato)
                self.ultimo += 1
                print("Contato inserido com sucesso!")
            else:
                print("A agenda está cheia. Não é possível adicionar mais contatos.")

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
            self.ultimo -= 1
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)
            print("------------------")

    def salvar_agenda(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self, arquivo)
        print("Agenda salva com sucesso!")

    @staticmethod
    def carregar_agenda(nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                agenda = pickle.load(arquivo)
            return agenda
        except FileNotFoundError:
            print("Arquivo não encontrado. Uma nova agenda será criada.")
            return Agenda()

def exibir_menu():
    print("===== MENU =====")
    print("1. Buscar contato")
    print("2. Inserir/Atualizar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Salvar agenda")
    print("6. Carregar agenda")
    print("0. Sair")
    print("================")

if __name__ == '__main__':
    agenda = Agenda()

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome (ou parte dele) do contato a ser buscado: ")
            contato = agenda.buscar_contato(nome)
            if contato:
                print("Contato encontrado:")
                print(contato)
            else:
                print("Contato não encontrado.")

        elif opcao == '2':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            endereco = input("Digite o endereço do contato: ")
            relacao = input("Digite a relação do contato: ")
            agenda.inserir_alterar_contato(nome, telefone, endereco, relacao)

        elif opcao == '3':
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)

        elif opcao == '4':
            agenda.listar_contatos()

        elif opcao == '5':
            nome_arquivo = input("Digite o nome do arquivo para salvar a agenda: ")
            agenda.salvar_agenda(nome_arquivo)

        elif opcao == '6':
            nome_arquivo = input("Digite o nome do arquivo para carregar a agenda: ")
            agenda = Agenda.carregar_agenda(nome_arquivo)

        elif opcao == '0':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Digite um número válido.")

        print()  # Linha em branco para separar as opções

