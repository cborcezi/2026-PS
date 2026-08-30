/*
 * Disciplina: 2026-PS
 * Estudante : Cauã Borcezi Ferreira
 * Data      : 2026.08.13
 * Projeto   : aula32-projeto-secretaria
 *Arquivo   : Aluno.java
 */

 
public class Aluno{
    private String nome;
    private String matricula;
    private String curso;
    private String email;


    public Aluno(String nome, String matricula, String curso, String email){
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
        this.email = email;    
    }

    public String getNome(){
        return nome;
    }

    public String getMatricula(){
        return matricula;
    }

    public String getCurso(){
        return curso;
    }

    public String getEmail(){
        return email;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setCurso(String curso){
        this.curso = curso;
    }

    @Override
    public String toString() {
        return matricula + " | " + nome + " | " + curso + " | " + email;
    }
}
