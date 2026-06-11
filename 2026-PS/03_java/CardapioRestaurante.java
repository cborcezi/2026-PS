import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;

public class CardapioRestaurante {
    static class Item {
        String nome;
        int quantidade;
        double preco;

        Item(String nome, int quantidade, double preco) {
            this.nome = nome;
            this.quantidade = quantidade;
            this.preco = preco;
        }

        double subtotal() {
            return quantidade * preco;
        }
    }

    public static void alterar_pedido(Scanner entrada, ArrayList<Item> carrinho) {
        System.out.println("\n===== ALTERAR PEDIDO =====");
        System.out.println("1 - Adicionar produto");
        System.out.println("2 - Remover produto");
        System.out.println("3 - Voltar");
        System.out.print("Escolha: ");
        int escolha = entrada.nextInt();
        if (escolha == 1) {

            System.out.println("\n1 - X-Burguer R$18");
            System.out.println("2 - Pizza R$35");
            System.out.println("3 - Suco Natural R$8");
            System.out.println("4 - Café R$5");
            System.out.println("5 - Salada R$12");
            System.out.print("Produto: ");
            int op = entrada.nextInt();
            String nome = "";
            double preco = 0;
            if (op == 1) {
                nome = "X-Burguer";
                preco = 18;
            } else if (op == 2) {
                nome = "Pizza";
                preco = 35;
            } else if (op == 3) {
                nome = "Suco Natural";
                preco = 8;
            } else if (op == 4) {
                nome = "Café";
                preco = 5;
            } else if (op == 5) {
                nome = "Salada";
                preco = 12;
            } else {
                System.out.println("Produto inválido!");
                return;
            }
            System.out.print("Quantidade: ");
            int qtd = entrada.nextInt();
            carrinho.add(new Item(nome, qtd, preco));
            System.out.println("Produto adicionado!");
        }

        else if (escolha == 2) {
            if (carrinho.size() == 0) {
                System.out.println("Pedido vazio!");
                return;
            }
            System.out.println("\nProdutos:");
            for (int i = 0; i < carrinho.size(); i++) {
                System.out.println(
                        (i + 1) + " - " + carrinho.get(i).nome);
            }
            System.out.print("Remover qual item? ");
            int remover = entrada.nextInt();
            if (remover >= 1 && remover <= carrinho.size()) {
                Item removido = carrinho.remove(remover - 1);
                System.out.println(
                        removido.nome + " removido!");

            } else {
                System.out.println("Número inválido!");
            }
        }
    }

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random random = new Random();
        ArrayList<Item> carrinho = new ArrayList<>();
        boolean montando = true;
        while (montando) {

            System.out.println("\n=================================");
            System.out.println("        RESTAURANTE DO IF");
            System.out.println("=================================");
            System.out.println("1 - Brownie - R$12");
            System.out.println("2 - Café - R$5");
            System.out.println("3 - Coxinha - R$8");
            System.out.println("4 - Milkshake - R$18");
            System.out.println("5 - Pastel - R$10");
            System.out.println("6 - Pizza - R$35");
            System.out.println("7 - Suco Natural - R$8");
            System.out.println("8 - X-Burguer - R$18");
            System.out.println("0 - Finalizar pedido");
            System.out.print("Escolha: ");
            int op = entrada.nextInt();

            String nome = "";
            double preco = 0;

            if (op == 1) {
                nome = "Brownie";
                preco = 12;
            } else if (op == 2) {
                nome = "Café";
                preco = 5;
            } else if (op == 3) {
                nome = "Coxinha";
                preco = 8;
            } else if (op == 4) {
                nome = "Milkshake";
                preco = 18;
            } else if (op == 5) {
                nome = "Pastel";
                preco = 10;
            } else if (op == 6) {
                nome = "Pizza";
                preco = 35;
            } else if (op == 7) {
                nome = "Suco Natural";
                preco = 8;
            } else if (op == 8) {
                nome = "X-Burguer";
                preco = 18;
            } else if (op == 0) {
                montando = false;
                continue;
            } else {
                System.out.println("Opção inválida!");
                continue;
            }

            System.out.print("Quantidade: ");
            int qtd = entrada.nextInt();
            carrinho.add(
                    new Item(nome, qtd, preco));
            System.out.println("Produto adicionado!");
        }

        while (true) {
            double total = 0;
            System.out.println("\n===========================");
            System.out.println("      RESUMO DO PEDIDO");
            System.out.println("===========================");
            for (int i = 0; i < carrinho.size(); i++) {
                Item it = carrinho.get(i);
                total += it.subtotal();
                System.out.printf(
                        "%d - %dx %s - R$ %.2f%n",
                        i + 1,
                        it.quantidade,
                        it.nome,
                        it.subtotal());
            }
            System.out.printf(
                    "\nTOTAL: R$ %.2f%n",
                    total);

            System.out.println("\n1 - Confirmar pedido");
            System.out.println("2 - Alterar pedido");
            System.out.print("Escolha: ");
            int op = entrada.nextInt();
            if (op == 1) {
                break;
            } else if (op == 2) {
                alterar_pedido(
                        entrada,
                        carrinho);
            } else {
                System.out.println("Opção inválida!");
            }
        }
        while (true) {
            double total = 0;
            System.out.println("\n===========================");
            System.out.println("        PAGAMENTO");
            System.out.println("===========================");
            for (Item it : carrinho) {
                total += it.subtotal();
            }
            System.out.printf(
                    "TOTAL: R$ %.2f%n",
                    total);
            System.out.println("\n1 - Dinheiro");
            System.out.println("2 - Cartão");
            System.out.println("3 - PIX");
            System.out.println("4 - Alterar pedido");
            System.out.print("Escolha: ");
            int pagamento = entrada.nextInt();
            if (pagamento == 4) {
                alterar_pedido(
                        entrada,
                        carrinho);
                continue;
            }
            if (pagamento == 1) {
                double valor;
                do {
                    System.out.print(
                            "Valor recebido: R$ ");
                    valor = entrada.nextDouble();
                    if (valor < total) {
                        System.out.println(
                                "Valor insuficiente!");
                    }
                } while (valor < total);
                System.out.printf(
                        "Troco: R$ %.2f%n",
                        valor - total);
                break;
            } else if (pagamento == 2) {
                System.out.println(
                        "Pagamento no cartão realizado!");
                break;
            } else if (pagamento == 3) {

                System.out.println(
                        "Pagamento via PIX realizado!");

                break;
            } else {
                System.out.println(
                        "Opção inválida!");
            }

        }
        int numeroPedido = random.nextInt(9000) + 1000;
        System.out.println(
                "\nPedido Nº " + numeroPedido);
        System.out.println(
                "Aguarde a chamada do seu pedido.");
        entrada.close();

    }
}