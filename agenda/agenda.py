import pickle
import tkinter as tk
from tkinter import messagebox

class Contato:
    def _init_(self, nome, telefone, endereco, relacao):  # Define o construtor da classe Contato
        self.nome = nome  # Atribui o valor do parâmetro nome ao atributo nome do objeto
        self.telefone = telefone  # Atribui o valor do parâmetro telefone ao atributo telefone do objeto
        self.endereco = endereco  # Atribui o valor do parâmetro endereco ao atributo endereco do objeto
        self.relacao = relacao  # Atribui o valor do parâmetro relacao ao atributo relacao do objeto

    def _str(self):  # Define o método especial __str_ para retornar uma representação em string do objeto
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\nRelação: {self.relacao}"

class Agenda:
    def _init_(self):  # Define o construtor da classe Agenda
        self.contatos = []  # Inicializa a lista de contatos como vazia
        self.ultimo = -1  # Inicializa o atributo ultimo com o valor -1

    def buscar_contato(self, nome):  # Define o método buscar_contato que recebe um nome como parâmetro
        for contato in self.contatos:  # Itera sobre a lista de contatos
            if nome.lower() in contato.nome.lower():  # Verifica se o nome (ignorando maiúsculas e minúsculas) está presente no nome do contato
                return contato  # Retorna o contato encontrado
        return None  # Retorna None caso nenhum contato seja encontrado

    def inserir_alterar_contato(self, nome, telefone, endereco, relacao):  # Define o método inserir_alterar_contato que recebe os dados de um contato como parâmetros
        contato = self.buscar_contato(nome)  # Busca o contato pelo nome
        if contato:  # Se o contato for encontrado
            contato.telefone = telefone  # Atualiza os atributos do contato com os novos valores
            contato.endereco = endereco
            contato.relacao = relacao
            print("Contato atualizado com sucesso!")
        else:  # Caso contrário
            if len(self.contatos) < 1000:  # Verifica se ainda há espaço para adicionar contatos na agenda
                novo_contato = Contato(nome, telefone, endereco, relacao)  # Cria um novo objeto Contato com os valores fornecidos
                self.contatos.append(novo_contato)  # Adiciona o novo contato à lista de contatos
                self.ultimo += 1  # Atualiza o valor do atributo ultimo
                print("Contato inserido com sucesso!")
            else:
                print("A agenda está cheia. Não é possível adicionar mais contatos.")

    def remover_contato(self, nome):  # Define o método remover_contato que recebe um nome como parâmetro
        contato = self.buscar_contato(nome)  # Busca o contato pelo nome
        if contato:  # Se o contato for encontrado
            self.contatos.remove(contato)  # Remove o contato da lista de contatos
            self.ultimo -= 1  # Atualiza o valor do atributo ultimo
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    def listar_contatos(self):  # Define o método listar_contatos
        for contato in self.contatos:  # Itera sobre a lista de contatos
            print(contato)  # Imprime as informações do contato
            print("------------------")

    def salvar_agenda(self, nome_arquivo):  # Define o método salvar_agenda que recebe um nome de arquivo como parâmetro
        with open(nome_arquivo, 'wb') as arquivo:  # Abre o arquivo no modo de escrita binária
            pickle.dump(self, arquivo)  # Serializa o objeto atual (agenda) e o escreve no arquivo
        print("Agenda salva com sucesso!")

    @staticmethod
    def carregar_agenda(nome_arquivo):  # Define o método estático carregar_agenda que recebe um nome de arquivo como parâmetro
        try:
            with open(nome_arquivo, 'rb') as arquivo:  # Abre o arquivo no modo de leitura binária
                agenda = pickle.load(arquivo)  # Desserializa o objeto armazenado no arquivo
            return agenda  # Retorna a agenda desserializada
        except FileNotFoundError:  # Trata a exceção de arquivo não encontrado
            print("Arquivo não encontrado. Uma nova agenda será criada.")
            return Agenda()  # Retorna uma nova instância de Agenda

def exibir_menu():  # Define a função exibir_menu
    print("===== MENU =====")
    print("1. Buscar contato")
    print("2. Inserir/Atualizar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Salvar agenda")
    print("6. Carregar agenda")
    print("0. Sair")
    print("================")

if __name__ == '__main__':  # Verifica se o código está sendo executado como script principal
    agenda = Agenda()  # Cria uma nova instância de Agenda

    while True:  # Loop principal do programa
        exibir_menu()  # Exibe o menu de opções
        opcao = input("Digite a opção desejada: ")  # Lê a opção digitada pelo usuário

        if opcao == '1':  # Opção de buscar contato
            nome = input("Digite o nome (ou parte dele) do contato a ser buscado: ")
            contato = agenda.buscar_contato(nome)  # Busca o contato na agenda
            if contato:  # Se o contato for encontrado
                print("Contato encontrado:")
                print(contato)  # Exibe as informações do contato
            else:
                print("Contato não encontrado.")

        elif opcao == '2':  # Opção de inserir/alterar contato
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            endereco = input("Digite o endereço do contato: ")
            relacao = input("Digite a relação do contato: ")
            agenda.inserir_alterar_contato(nome, telefone, endereco, relacao)  # Insere ou atualiza o contato na agenda

        elif opcao == '3':  # Opção de remover contato
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)  # Remove o contato da agenda

        elif opcao == '4':  # Opção de listar contatos
            agenda.listar_contatos()  # Lista os contatos da agenda

        elif opcao == '5':  # Opção de salvar agenda
            nome_arquivo = input("Digite o nome do arquivo para salvar a agenda: ")
            agenda.salvar_agenda(nome_arquivo)  # Salva a agenda em um arquivo

        elif opcao == '6':  # Opção de carregar agenda
            nome_arquivo = input("Digite o nome do arquivo para carregar a agenda: ")
            agenda = Agenda.carregar_agenda(nome_arquivo)  # Carrega a agenda de um arquivo

        elif opcao == '0':  # Opção de sair
            print("Encerrando o programa...")
            break  # Encerra o loop

        else:
            print("Opção inválida. Digite um número válido.")

        print()  # Linha em branco para separar as opções

class ContactManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.agenda = Agenda()

        self.create_widgets()

    def create_widgets(self):
        # Labels and entry fields for contact details
        self.label_name = tk.Label(self.root, text="Name:")
        self.entry_name = tk.Entry(self.root)

        self.label_phone = tk.Label(self.root, text="Phone:")
        self.entry_phone = tk.Entry(self.root)

        self.label_address = tk.Label(self.root, text="Address:")
        self.entry_address = tk.Entry(self.root)

        self.label_relation = tk.Label(self.root, text="Relation:")
        self.entry_relation = tk.Entry(self.root)

        # Buttons to perform actions
        self.button_search = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.button_add_update = tk.Button(self.root, text="Add/Update Contact", command=self.add_update_contact)
        self.button_remove = tk.Button(self.root, text="Remove Contact", command=self.remove_contact)
        self.button_list = tk.Button(self.root, text="List Contacts", command=self.list_contacts)
        self.button_save = tk.Button(self.root, text="Save Agenda", command=self.save_agenda)
        self.button_load = tk.Button(self.root, text="Load Agenda", command=self.load_agenda)
        self.button_exit = tk.Button(self.root, text="Exit", command=self.root.quit)

        # Layout using grid
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_address.grid(row=2, column=0, padx=5, pady=5)
        self.entry_address.grid(row=2, column=1, padx=5, pady=5)

        self.label_relation.grid(row=3, column=0, padx=5, pady=5)
        self.entry_relation.grid(row=3, column=1, padx=5, pady=5)

        self.button_search.grid(row=4, column=0, padx=5, pady=5)
        self.button_add_update.grid(row=4, column=1, padx=5, pady=5)
        self.button_remove.grid(row=4, column=2, padx=5, pady=5)
        self.button_list.grid(row=5, column=0, padx=5, pady=5)
        self.button_save.grid(row=5, column=1, padx=5, pady=5)
        self.button_load.grid(row=5, column=2, padx=5, pady=5)
        self.button_exit.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

    def search_contact(self):
        name = self.entry_name.get().strip()
        if name:
            contact = self.agenda.buscar_contato(name)
            if contact:
                messagebox.showinfo("Contact Found", str(contact))
            else:
                messagebox.showinfo("Contact Not Found", "No contact found with the given name.")
        else:
            messagebox.showwarning("Missing Information", "Please enter a name to search.")

    def add_update_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        address = self.entry_address.get().strip()
        relation = self.entry_relation.get().strip()

        if name:
            self.agenda.inserir_alterar_contato(name, phone, address, relation)
            messagebox.showinfo("Success", "Contact added/updated successfully.")
        else:
            messagebox.showwarning("Missing Information", "Please enter a name to add/update contact.")

    def remove_contact(self):
        name = self.entry_name.get().strip()
        if name:
            self.agenda.remover_contato(name)
            messagebox.showinfo("Success", "Contact removed successfully.")
        else:
            messagebox.showwarning("Missing Information", "Please enter a name to remove contact.")

    def list_contacts(self):
        contacts = self.agenda.contatos
        if contacts:
            contact_list = "\n".join(str(contact) for contact in contacts)
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts in the agenda.")

    def save_agenda(self):
        file_name = tk.filedialog.asksaveasfilename(defaultextension=".dat", filetypes=[("Data Files", "*.dat")])
        if file_name:
            self.agenda.salvar_agenda(file_name)
            messagebox.showinfo("Success", "Agenda saved successfully.")

    def load_agenda(self):
        file_name = tk.filedialog.askopenfilename(filetypes=[("Data Files", "*.dat")])
        if file_name:
            self.agenda = Agenda.carregar_agenda(file_name)
            messagebox.showinfo("Success", "Agenda loaded successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerGUI(root)
    root.mainloop()
