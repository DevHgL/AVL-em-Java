package agenda;

public class Principal {
    public static void main(String[] args) {
        Agenda agenda = new Agenda();

        // Adicionando contatos
        Contato contato1 = new Contato("João", "123456789", "Rua A, 123", "Amigo");
        Contato contato2 = new Contato("Maria", "987654321", "Rua B, 456", "Família");
        Contato contato3 = new Contato("José", "555555555", "Rua C, 789", "Trabalho");

        agenda.adicionarContato(contato1);
        agenda.adicionarContato(contato2);
        agenda.adicionarContato(contato3);

        // Buscando contato
        Contato resultadoBusca = agenda.buscarContato("Ma");
        if (resultadoBusca != null) {
            System.out.println("Contato encontrado:\n" + resultadoBusca);
        } else {
            System.out.println("Contato não encontrado.");
        }

        // Removendo contato
        boolean removido = agenda.removerContato("João");
        if (removido) {
            System.out.println("Contato removido com sucesso.");
        } else {
            System.out.println("Contato não encontrado.");
        }

        // Listando contatos
        agenda.listarContatos();

        // Salvando e recuperando agenda
        agenda.salvarAgenda("agenda.dat");

        Agenda agendaRecuperada = new Agenda();
        agendaRecuperada.recuperarAgenda("agenda.dat");

        System.out.println("\nAgenda recuperada:");
        agendaRecuperada.listarContatos();
    }
}