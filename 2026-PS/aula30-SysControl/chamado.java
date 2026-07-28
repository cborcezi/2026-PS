public class chamado {

    private int numero;
    private String descricao;
    private int prioridade; // 1 = Baixa | 2 = Média | 3 = Alta
    private boolean aberto;

    public chamado(int numero, String descricao, int prioridade, boolean aberto) {
        if (numero <= 0) {
            throw new IllegalArgumentException("Número deve ser positivo.");
        }
        if (descricao == null || descricao.trim().isEmpty()) {
            throw new IllegalArgumentException("Descrição não pode ser vazia.");
        }
        if (prioridade < 1 || prioridade > 3) {
            throw new IllegalArgumentException("Prioridade deve ser entre 1 e 3.");
        }
        this.numero = numero;
        this.descricao = descricao;
        this.prioridade = prioridade;
        this.aberto = aberto;
    }
    public int getNumero() {
        return numero;
    }
    public String getDescricao() {
        return descricao;
    }
    public int getPrioridade() {
        return prioridade;
    }
    public boolean isAberto() {
        return aberto;
    }
    public boolean setDescricao(String descricao) {
        if (descricao == null || descricao.trim().isEmpty()) {
            return false;
        }
        this.descricao = descricao;
        return true;
    }
    public boolean alterarPrioridade(int prioridade) {
        if (prioridade < 1 || prioridade > 3) {
            return false;
        }
        this.prioridade = prioridade;
        return true;
    }
    public boolean fechar() {
        if (!aberto) {
            return false;
        }
        aberto = false;
        return true;
    }
    public boolean reabrir() {
        if (aberto) {
            return false;
        }
        aberto = true;
        return true;
    }

    // ----------- DESAFIO EXTRA 1 -------------
    public String resumo() {
        return "Chamado Nº " + numero +
                " | " + descricao +
                " | Prioridade: " + prioridade +
                " | Aberto: " + aberto;
    }
    // ----------- DESAFIO EXTRA 2 -------------
    public boolean atualizarDescricaoEPrioridade(String descricao, int prioridade) {
        if (descricao == null || descricao.trim().isEmpty()) {
            return false;
        }
        if (prioridade < 1 || prioridade > 3) {
            return false;
        }
        this.descricao = descricao;
        this.prioridade = prioridade;
        return true;
    }
}