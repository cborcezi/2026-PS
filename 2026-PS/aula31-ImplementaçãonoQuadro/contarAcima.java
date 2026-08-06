import java.util.Scanner;
public class contarAcima {
    int Acima(int[] numeros, int limite) {
        int contador = 0;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] > limite) {
                contador++;
            }
        }
        return contador;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Quantos números deseja digitar? ");
        int quantidade = sc.nextInt();
        int[] numeros = new int[quantidade];
        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = sc.nextInt();
        }
        System.out.print("Digite o limite: ");
        int limite = sc.nextInt();
        contarAcima obj = new contarAcima();
        System.out.print("Números acima do limite: ");
        System.out.println(obj.Acima(numeros, limite));
        sc.close();
    }
}