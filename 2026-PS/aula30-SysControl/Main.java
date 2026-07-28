public class Main {
    public static void main(String[] args) {
        chamado c1 = new chamado(
                15,
                "Jo - Computador sem ligar",
                2,
                true);
        chamado c2 = new chamado(
                115,
                "Jo - Internet lenta",
                3,
                true);
        chamado c3 = new chamado(
                215,
                "Jo - Impressora travada",
                1,
                false);

        System.out.println("=== Objetos Criados ===");
        System.out.println(c1.resumo());
        System.out.println(c2.resumo());
        System.out.println(c3.resumo());
        System.out.println();
        System.out.println("===== Teste inválido =====");
        if (!c1.setDescricao("")) {
            System.out.println("Descrição inválida.");
        }
        System.out.println();
        System.out.println("===== Prioridade inválida =====");
        if (!c2.alterarPrioridade(5)) {
            System.out.println("Prioridade recusada.");
        }
        System.out.println();
        System.out.println("===== Fechando chamado =====");
        if (c1.fechar()) {
            System.out.println("Chamado fechado.");
        }
        System.out.println();
        System.out.println("===== Tentando fechar novamente =====");
        if (!c1.fechar()) {
            System.out.println("Operação inválida.");
        }
        System.out.println();
        System.out.println("===== Atualizando descrição e prioridade =====");
        if (c3.atualizarDescricaoEPrioridade(
                "Jo - Impressora funcionando",
                2)) {
            System.out.println("Atualização realizada.");
        }
        System.out.println();
        System.out.println("===== Estado Final =====");
        System.out.println(c1.resumo());
        System.out.println(c2.resumo());
        System.out.println(c3.resumo());

    }
}