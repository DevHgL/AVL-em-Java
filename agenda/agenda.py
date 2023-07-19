import pickle
import tkinter as tk
from tkinter import messagebox

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
            messagebox.showinfo("Contato atualizado", "Contato atualizado com sucesso!")
        else:
            if len(self.contatos) < 1000:
                novo_contato = Contato(nome, telefone, endereco, relacao)
                self.contatos.append(novo_contato)
                self.ultimo += 1
                messagebox.showinfo("Contato inserido", "Contato inserido com sucesso!")
            else:
                messagebox.showwarning("Agenda cheia", "A agenda está cheia. Não é possível adicionar mais contatos.")

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
            self.ultimo -= 1
            messagebox.showinfo("Contato removido", "Contato removido com sucesso!")
        else:
            messagebox.showwarning("Contato não encontrado", "Contato não encontrado.")

    def listar_contatos(self):
        return '\n'.join([str(contato) for contato in self.contatos])

    def salvar_agenda(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self, arquivo)
        messagebox.showinfo("Agenda salva", "Agenda salva com sucesso!")

    @staticmethod
    def carregar_agenda(nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                agenda = pickle.load(arquivo)
            return agenda
        except FileNotFoundError:
            messagebox.showwarning("Arquivo não encontrado", "Arquivo não encontrado. Uma nova agenda será criada.")
            return Agenda()
        
agenda = Agenda()

def buscar_contato():
    nome = nome_entry.get()
    contato = agenda.buscar_contato(nome)
    if contato:
        informacoes_text.delete(1.0, tk.END)
        informacoes_text.insert(tk.END, str(contato))
    else:
        informacoes_text.delete(1.0, tk.END)
        informacoes_text.insert(tk.END, "Contato não encontrado.")

def inserir_alterar_contato():
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    endereco = endereco_entry.get()
    relacao = relacao_entry.get()
    agenda.inserir_alterar_contato(nome, telefone, endereco, relacao)

def remover_contato():
    nome = nome_entry.get()
    agenda.remover_contato(nome)

def listar_contatos():
    contatos_info = agenda.listar_contatos()
    informacoes_text.delete(1.0, tk.END)
    informacoes_text.insert(tk.END, contatos_info)

def salvar_agenda():
    nome_arquivo = nome_arquivo_entry.get()
    agenda.salvar_agenda(nome_arquivo)

def carregar_agenda():
    nome_arquivo = nome_arquivo_entry.get()
    global agenda
    agenda = Agenda.carregar_agenda(nome_arquivo)

def exibir_menu():
    informacoes_text.delete(1.0, tk.END)
    informacoes_text.insert(tk.END, "===== MENU =====\n"
                                   "1. Buscar contato\n"
                                   "2. Inserir/Atualizar contato\n"
                                   "3. Remover contato\n"
                                   "4. Listar contatos\n"
                                   "5. Salvar agenda\n"
                                   "6. Carregar agenda\n"
                                   "0. Sair\n"
                                   "================")

app = tk.Tk()
app.title("Agenda Telefônica")
app.geometry("600x400")

nome_label = tk.Label(app, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5)
nome_entry = tk.Entry(app)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

telefone_label = tk.Label(app, text="Telefone:")
telefone_label.grid(row=1, column=0, padx=5, pady=5)
telefone_entry = tk.Entry(app)
telefone_entry.grid(row=1, column=1, padx=5, pady=5)

endereco_label = tk.Label(app, text="Endereço:")
endereco_label.grid(row=2, column=0, padx=5, pady=5)
endereco_entry = tk.Entry(app)
endereco_entry.grid(row=2, column=1, padx=5, pady=5)

relacao_label = tk.Label(app, text="Relação:")
relacao_label.grid(row=3, column=0, padx=5, pady=5)
relacao_entry = tk.Entry(app)
relacao_entry.grid(row=3, column=1, padx=5, pady=5)

informacoes_text = tk.Text(app, height=10, width=50)
informacoes_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

nome_arquivo_label = tk.Label(app, text="Nome do arquivo:")
nome_arquivo_label.grid(row=5, column=0, padx=5, pady=5)
nome_arquivo_entry = tk.Entry(app)
nome_arquivo_entry.grid(row=5, column=1, padx=5, pady=5)

buscar_button = tk.Button(app, text="Buscar", command=buscar_contato)
buscar_button.grid(row=0, column=2, padx=5, pady=5)

inserir_button = tk.Button(app, text="Inserir/Atualizar", command=inserir_alterar_contato)
inserir_button.grid(row=1, column=2, padx=5, pady=5)

remover_button = tk.Button(app, text="Remover", command=remover_contato)
remover_button.grid(row=2, column=2, padx=5, pady=5)

listar_button = tk.Button(app, text="Listar", command=listar_contatos)
listar_button.grid(row=3, column=2, padx=5, pady=5)

salvar_button = tk.Button(app, text="Salvar", command=salvar_agenda)
salvar_button.grid(row=5, column=2, padx=5, pady=5)

carregar_button = tk.Button(app, text="Carregar", command=carregar_agenda)
carregar_button.grid(row=5, column=3, padx=5, pady=5)

sair_button = tk.Button(app, text="Sair", command=app.quit)
sair_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

exibir_menu()

app.mainloop()
