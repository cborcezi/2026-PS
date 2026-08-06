import java.util.Scanner;
public class calculaSoma {
    int soma(int[] numeros) {
        int soma = 0;
        for (int i = 0; i < numeros.length; i++) {
            soma += numeros[i];
        }
        return soma;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Quantos números deseja digitar? ");
        int quantidade = sc.nextInt();
        int[] numeros = new int[quantidade];
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Digite o " + (i + 1) + "º número: ");
            numeros[i] = sc.nextInt();
        }
        calculaSoma obj = new calculaSoma();
        System.out.println("Soma = " + obj.soma(numeros));
        sc.close();
    }
}