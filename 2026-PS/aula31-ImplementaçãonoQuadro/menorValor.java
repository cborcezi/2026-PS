import java.util.Scanner;
public class menorValor {
    int menor(int[] numeros) {
        int menor = numeros[0];
        for (int i = 1; i < numeros.length; i++) {
            if (numeros[i] < menor) {
                menor = numeros[i];
            }
        }
        return menor;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Quantos números deseja digitar? ");
        int quantidade = sc.nextInt();
        int[] numeros = new int[quantidade];
        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = sc.nextInt();
        }
        menorValor obj = new menorValor();
        System.out.print("Menor valor: ");
        System.out.println(obj.menor(numeros));
        sc.close();
    }
}