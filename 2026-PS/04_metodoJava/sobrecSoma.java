public class sobrecSoma {

    public static int somar(int a, int b) {
        return a + b;
    }

    public static double somar(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println(somar(5, 3));
        System.out.println(somar(2.5, 3.5));     
        System.out.println(somar(100, 50));     
    }
}