/*
* Disciplina: 2026-PS
* Projeto   : bibliotech
* Arquivo   : Livro.java 
* Autor     : Cauã Borcezi Ferreira
* Descricao : a caixa "Livro" do diagrama de classes, em Java (Aula 37).
*/
public class Livro {
    private String titulo;
    private String autor;
    private int ano;
    private boolean disponivel;  

    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAno() {
        return ano;
    }

    public boolean estaDisponivel() {
        return disponivel;
    }

    public void emprestar() {
        this.disponivel = false;
    }

    public void devolver() {
        this.disponivel = true;
    }

    public String toString() {
        String situacao = disponivel ? "disponivel" : "emprestado";
        return titulo + " (" + autor + ", " + ano + ") - " + situacao;
    }
}
