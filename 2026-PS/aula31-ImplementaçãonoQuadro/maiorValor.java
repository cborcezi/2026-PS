import java.util.Scanner;
public class maiorValor {
    int maior(int[] numeros) {
        int maior = numeros[0];
        for (int i = 1; i < numeros.length; i++) {
            if (numeros[i] > maior) {
                maior = numeros[i];
            }
        }
        return maior;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Quantos números deseja digitar? ");
        int quantidade = sc.nextInt();
        int[] numeros = new int[quantidade];
        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = sc.nextInt();
        }
        maiorValor obj = new maiorValor();
        System.out.print("Maior valor: ");
        System.out.println(obj.maior(numeros));
        sc.close();
    }
}