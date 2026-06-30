import java.util.Scanner;

public class exibirBoletim {

    static double calcularMedia(double[] notas) {
        double soma = 0;

        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }

        return soma / notas.length;
    }

    static int contarAprovados(double[] notas) {
        int aprovados = 0;

        for (int i = 0; i < notas.length; i++) {
            if (notas[i] >= 6) {
                aprovados++;
            }
        }

        return aprovados;
    }

    static void mostrarBoletim(double[] notas){
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);

        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);

        if (media >= 6) {
            System.out.println("Situação: APROVADO");
        } else {
            System.out.println("Situação: EM RECUPERAÇÃO");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantas notas deseja informar? ");
        int n = sc.nextInt();

        double[] notas = new double[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Digite a nota " + (i + 1) + ": ");
            notas[i] = sc.nextDouble();
        }

        mostrarBoletim(notas);

        sc.close();
    }
}