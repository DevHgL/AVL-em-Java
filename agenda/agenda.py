import pickle  # Importa o módulo pickle, utilizado para serializar e desserializar objetos Python

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

if __name__ == '_main_':  # Verifica se o código está sendo executado como script principal
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