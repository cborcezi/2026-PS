public class verificaMaior {

    public static int majorNumero(int a, int b) {
        return (a >= b) ? a : b;
    }

    public static void main(String[] args) {
        System.out.println(majorNumero(10, 20));
        System.out.println(majorNumero(50, 5));
        System.out.println(majorNumero(30, 30));
    }
}