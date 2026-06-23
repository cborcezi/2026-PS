public class sistemCardapio {

    public static void exibirProduto(String nome) {
        System.out.println("Produto: " + nome);
    }

    public static void exibirProduto(String nome, double preco) {
        System.out.println("Produto: " + nome);
        System.out.println("Preço: R$ " + String.format("%.2f", preco));
    }

    public static void main(String[] args) {
        exibirProduto("Refrigerante");
        System.out.println();

        exibirProduto("Pizza", 39.90);
        System.out.println();

        exibirProduto("Hambúrguer", 22.50);
    }
}