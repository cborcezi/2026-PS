import java.util.Scanner;

public class mediaTurma {

    static double calcularMedia(double[] notas) {
        double soma = 0;

        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }

        return soma / notas.length;
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

        double media = calcularMedia(notas);

        System.out.println("Média da turma: " + media);

        sc.close();
    }
}