public class multiply {

    static int dobro(int numero) {
        return numero * 2;
    }

    static int triplo(int numero) {
        return numero * 3;
    }

    public static void main(String[] args) {

        int resultadoDobro = dobro(10);
        int resultadoTriplo = triplo(10);

        System.out.println("Dobro: " + resultadoDobro);
        System.out.println("Triplo: " + resultadoTriplo);
    }
}