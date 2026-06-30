import java.util.Scanner;

public class contarAprova {

    static int contarAprovados(double[] notas) {
        int aprovados = 0;

        for (int i = 0; i < notas.length; i++) {
            if (notas[i] >= 6.0) {
                aprovados++;
            }
        }

        return aprovados;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantas notas deseja informar? ");
        int quantidade = sc.nextInt();

        double[] notas = new double[quantidade];

        for (int i = 0; i < quantidade; i++) {
            System.out.print("Digite a nota " + (i + 1) + ": ");
            notas[i] = sc.nextDouble();
        }

        int totalAprovados = contarAprovados(notas);

        System.out.println("Quantidade de aprovados: " + totalAprovados);

        sc.close();
    }
}