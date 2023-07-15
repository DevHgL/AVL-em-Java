package agenda;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

class Contato {
    private String nome;
    private String telefone;
    private String endereco;
    private String relacao;

    public Contato(String nome, String telefone, String endereco, String relacao) {
        this.nome = nome;
        this.telefone = telefone;
        this.endereco = endereco;
        this.relacao = relacao;
    }

    public String getNome() {
        return nome;
    }

    public String getTelefone() {
        return telefone;
    }

    public String getEndereco() {
        return endereco;
    }

    public String getRelacao() {
        return relacao;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public void setRelacao(String relacao) {
        this.relacao = relacao;
    }

    @Override
    public String toString() {
        return ("Nome: " + nome + "\n" + "Telefone: " + telefone + "\n" + "Endereço: " + endereco + "\n" + 
               "Relação: " + relacao + "\n");
    }
}

class Agenda {
    private List<Contato> contatos;
    private int ultimo;

    public Agenda() {
        contatos = new ArrayList<>();
        ultimo = -1;
    }

    public boolean adicionarContato(Contato contato) {
        if (contatoExistente(contato.getNome())) {
            return false; // Já existe um contato com esse nome
        }
        contatos.add(contato);
        ultimo++;
        return true;
    }

    public boolean removerContato(String nome) {
        for (int i = 0; i <= ultimo; i++) {
            if (contatos.get(i).getNome().equalsIgnoreCase(nome)) {
                contatos.remove(i);
                ultimo--;
                return true;
            }
        }
        return false; // Contato não encontrado
    }

    public Contato buscarContato(String nome) {
        for (int i = 0; i <= ultimo; i++) {
            if (contatos.get(i).getNome().toLowerCase().contains(nome.toLowerCase())) {
                return contatos.get(i);
            }
        }
        return null; // Contato não encontrado
    }

    public void listarContatos() {
        for (int i = 0; i <= ultimo; i++) {
            System.out.println(contatos.get(i));
        }
    }

    public void salvarAgenda(String nomeArquivo) {
        try {
            FileOutputStream fileStream = new FileOutputStream(nomeArquivo);
            ObjectOutputStream objectStream = new ObjectOutputStream(fileStream);
            objectStream.writeObject(contatos);
            objectStream.close();
            fileStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void recuperarAgenda(String nomeArquivo) {
        try {
            FileInputStream fileStream = new FileInputStream(nomeArquivo);
            ObjectInputStream objectStream = new ObjectInputStream(fileStream);
            contatos = (List<Contato>) objectStream.readObject();
            ultimo = contatos.size() - 1;
            objectStream.close();
            fileStream.close();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    private boolean contatoExistente(String nome) {
        for (int i = 0; i <= ultimo; i++) {
            if (contatos.get(i).getNome().equalsIgnoreCase(nome)) {
                return true;
            }
        }
        return false;
    }
}

