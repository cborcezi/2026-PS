public class calcDesconto {

    static double calcularDesconto(double valor, double percentual) {
        double desconto = valor * (percentual / 100);
        return valor - desconto;
    }

    public static void main(String[] args) {

        System.out.println(calcularDesconto(100, 10));
        System.out.println(calcularDesconto(250, 20));
        System.out.println(calcularDesconto(500, 15));

    }
}