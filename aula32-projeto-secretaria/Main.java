/*
 * Disciplina: 2026-PS
 * Estudante : Cauã Borcezi Ferreira
 * Data      : 2026.08.13
 * Projeto   : aula32-projeto-secretaria
 *Arquivo    : Main.java
 */


import java.util.ArrayList;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);

        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while(true){
            System.out.println("==========================================================");
            System.out.println("     SECRETARIA DO CAMPUS - por Cauã Borcezi Ferreira");
            System.out.println("==========================================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matrícula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {
                System.out.println("Atendimento encerrado. A secretaria agradece sua visita. Até a próxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else if (opcao.equals("3")) {
                buscar(lista, teclado);
            } else if (opcao.equals("4")) {
                atualizar(lista, teclado);
            } else if (opcao.equals("5")) {
                remover(lista, teclado);
            } else if (opcao.equals("6")) {
                relatorio(lista, teclado);    
            } else {
                System.out.println("Opcao invalida! Vale 0, 1, 2, 3, 4, 5 ou 6.");
            }
        }
    }

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        Aluno existente = buscarPorMatricula(lista, matricula);
        if (existente != null) {
            System.out.println("Cadastro invalido. A matricula " + matricula + " ja existe!");
            return;
        }

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        System.out.print("E-mail: ");
        String email = teclado.nextLine().trim();
        
        Aluno novoAluno = new Aluno(nome, matricula, curso, email);
        lista.add(novoAluno);

        System.out.println("Cadastro de " + novoAluno.getNome() + " realizado com sucesso!");
    }

    static void listar(ArrayList<Aluno> lista){
        if (lista.size() == 0) {
        System.out.println("Nenhuma ficha encontrada no sistema!");
        return;
        }
        System.out.println("--- FICHAS NO SISTEMA: " + lista.size() + " ---");
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            System.out.println(a);
            
        }
    }

    static Aluno buscarPorMatricula(ArrayList<Aluno> lista, String matricula){
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            if (a.getMatricula().equals(matricula)) {
                return a;
            }
        }
        return null;
    }

    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matrícula procurada: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);

        if(a == null) {
            System.out.println("Nenhuma ficha encontrada para a matricula " + matricula + "!");
        }else {
            System.out.println("Ficha encontrada: " + a);

        }
    }

    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula a ser atualizada: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        
        if (a == null) {
            System.out.println("Nenhuma ficha encontrada para a matricula " + matricula + "!");
            return;
        }
        System.out.print("Informe o novo curso de " + a.getNome() + ": ");
        String novoCurso = teclado.nextLine().trim();
        
        a.setCurso(novoCurso);
        System.out.println("Ficha atualizada: " + a);
    }

    static void remover (ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Numero da matricula que deseja remover: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha encontrada para a matricula " + matricula + ".");
            return;
        }
        System.out.print("Tem certeza que deseja remover a ficha de  " + a.getNome() + "? (sim/nao): ");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("sim")) {
            lista.remove(a);
            System.out.println("Ficha de " +a.getNome() + " removida com sucesso!");
        } else {
            System.out.println("A remocao foi cancelada!");
        }
    }
    static void relatorio(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.println("--- RELATORIO DA SECRETARIA ---");
        System.out.println("Total de fichas: " + lista.size());
        System.out.print("Informe o curso para consultar a quantidade de alunos: ");
        String curso = teclado.nextLine().trim();

        int contador = 0;
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            if (a.getCurso().equals(curso)) {
                contador = contador + 1;
            }
        }
        System.out.println("Total de alunos no curso de " + curso + ": " + contador);
    }
}