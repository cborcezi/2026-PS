import java.util.ArrayList;
import java.util.Scanner;

public class catProduto {

    static void adicionarProduto(ArrayList<String> lista, String nome) {
        lista.add(nome);
    }

    static void listarProdutos(ArrayList<String> lista) {
        for (int i = 0; i < lista.size(); i++) {
            System.out.println((i + 1) + " - " + lista.get(i));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> produtos = new ArrayList<>();

        System.out.print("Quantos produtos deseja cadastrar? ");
        int quantidade = sc.nextInt();
        sc.nextLine(); // limpar buffer

        for (int i = 0; i < quantidade; i++) {
            System.out.print("Digite o nome do produto " + (i + 1) + ": ");
            String nome = sc.nextLine();

            adicionarProduto(produtos, nome);
        }

        System.out.println("\nCatálogo de Produtos:");
        listarProdutos(produtos);

        sc.close();
    }
}