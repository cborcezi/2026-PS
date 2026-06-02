import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("============================================");
        System.out.println(" CARDÁPIO ELETRÔNICO - RESTARAURANTE DO IF");
        System.out.println("============================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$ 8,00");
        System.out.println("4 - Café ............... R$ 5,00");
        System.out.println("5 - Salada ............. R$ 12,00");
        System.out.println("=================================");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        String nomeItem = "";
        double preco = 0;

        if (opcao == 1) {
            nomeItem = "X-Burguer";
            preco = 18.0;
        } else if (opcao == 2) {
            nomeItem = "Pizza";
            preco = 35.0;
        } else if (opcao == 3) {
            nomeItem = "Suco Natural";
            preco = 8.0;
        } else if (opcao == 4) {
            nomeItem = "Café";
            preco = 5.0;
        } else if (opcao == 5) {
            nomeItem = "Salada";
            preco = 12.0;
        } else {
            System.out.println("Opção inválida.");
            entrada.close();
            return;
        }

        System.out.print("Quantidade desejada: ");
        int quantidade = entrada.nextInt();

        double total = preco * quantidade;

        System.out.println("\nResumo do pedido:");
        System.out.println("Item: " + nomeItem);
        System.out.println("Preço unitário: R$ " + preco);
        System.out.println("Quantidade: " + quantidade);
        System.out.println("Total a pagar: R$ " + total);

        entrada.close();
    }
}