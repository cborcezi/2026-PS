/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Main.java
 * Autor     : Cauã Borcezi Ferreira
 * Descricao : BiblioTech (Aula 37): as classes do diagrama existem
 *             e se apresentam. O menu chega na Aula 39.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("BiblioTech v0.2 - as classes existem");

        Livro l1 = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        Livro l2 = new Livro("Capitaes da Areia", "Jorge Amado", 1937);
        Leitor pedro = new Leitor("Pedro Alves", "2026010", 3);
        Bibliotecario marli = new Bibliotecario("Marli Souza", "1998002", "F-0421");

        System.out.println(l1);
        System.out.println(l2);
        System.out.println(pedro);
        System.out.println(marli);

        System.out.println("Nome do leitor, via heranca: " + pedro.getNome());
        System.out.println("Pedro pode pegar livro? " + pedro.podePegarEmprestado());
        System.out.println("Marli entrou? " + marli.entrar());

        l1.emprestar();
        pedro.pegouLivro();
        System.out.println("Depois do emprestimo: " + l1);
        System.out.println("Depois do emprestimo: " + pedro);
    }
}