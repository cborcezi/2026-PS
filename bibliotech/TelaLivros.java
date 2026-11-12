
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.*;
import java.util.List;

public class TelaLivros extends JFrame {

        private final LivroDAO dao = new LivroDAO();

        private final DefaultTableModel modelo;
        private final JTable tabela;

        private final JTextField campoId = new JTextField(8);
        private final JLabel status = new JLabel("Pronto.");
        private final JTextField campoTitulo = new JTextField(18);

        // Cores da interface
        private final Color verde = new Color(0, 120, 45);
        private final Color verdeClaro = new Color(0, 150, 55);
        private final Color fundo = new Color(35, 39, 42);
        private final Color grafite = new Color(55, 60, 65);
        private final Color branco = new Color(255, 255, 255);
        private final Color corCampo = new Color(75, 82, 87);

        // Fontes da interface
        private final Font fontePadrao = new Font("Segoe UI", Font.PLAIN, 15);

        private final Font fonteTabela = new Font("Segoe UI", Font.PLAIN, 16);

        private final Font fonteNegrito = new Font("Segoe UI", Font.BOLD, 14);

        private final Font fonteCabecalho = new Font("Segoe UI", Font.BOLD, 16);

        public TelaLivros() {

                // Configuração das fontes padrão do Swing
                UIManager.put("Label.font", fonteNegrito);
                UIManager.put("Button.font", fonteNegrito);
                UIManager.put("TextField.font", fontePadrao);
                UIManager.put("Table.font", fonteTabela);
                UIManager.put("TableHeader.font", fonteCabecalho);
                UIManager.put("OptionPane.messageFont", fontePadrao);
                UIManager.put("OptionPane.buttonFont", fonteNegrito);

                setTitle("BiblioTech - Consulta de Livros");
                setSize(1050, 550);
                setLocationRelativeTo(null);

                setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                setLayout(new BorderLayout(0, 0));

                getContentPane().setBackground(fundo);

                modelo = new DefaultTableModel(
                                new Object[] {
                                                "ID", "Capa", "Título", "Autor", "Ano"
                                }, 0) {

                        @Override
                        public boolean isCellEditable(int linha, int coluna) {
                                return false;
                        }
                };

                // Configuração da tabela
                tabela = new JTable(modelo);

                tabela.setRowHeight(95);
                tabela.setFont(fonteTabela);
                tabela.setBackground(grafite);
                tabela.setForeground(new Color(245, 245, 245));
                tabela.setSelectionBackground(verdeClaro);
                tabela.setSelectionForeground(branco);
                tabela.setGridColor(new Color(115, 125, 130));
                tabela.setShowGrid(true);

                // Cabeçalho da tabela
                tabela.getTableHeader().setFont(fonteCabecalho);
                tabela.getTableHeader().setBackground(verde);
                tabela.getTableHeader().setForeground(branco);
                tabela.getTableHeader().setOpaque(true);

                // Largura das colunas
                tabela.getColumnModel().getColumn(0).setPreferredWidth(25);
                tabela.getColumnModel().getColumn(1).setPreferredWidth(100);
                tabela.getColumnModel().getColumn(2).setPreferredWidth(250);
                tabela.getColumnModel().getColumn(3).setPreferredWidth(250);
                tabela.getColumnModel().getColumn(4).setPreferredWidth(30);

                // Renderizador personalizado das células
                DefaultTableCellRenderer renderizador = new DefaultTableCellRenderer() {

                        @Override
                        public Component getTableCellRendererComponent(
                                        JTable tabela,
                                        Object valor,
                                        boolean selecionado,
                                        boolean foco,
                                        int linha,
                                        int coluna) {

                                Component componente = super.getTableCellRendererComponent(
                                                tabela,
                                                valor,
                                                selecionado,
                                                foco,
                                                linha,
                                                coluna);

                                componente.setFont(fonteTabela);

                                setHorizontalAlignment(SwingConstants.CENTER);

                                return componente;
                        }
                };

                // Aplicar o renderizador em todas as colunas
                for (int i = 0; i < tabela.getColumnCount(); i++) {
                        tabela.getColumnModel()
                                        .getColumn(i)
                                        .setCellRenderer(renderizador);
                }

                // Painel superior
                JPanel painelSuperior = new JPanel(
                                new GridLayout(2, 1, 5, 5));

                painelSuperior.setBackground(fundo);
                painelSuperior.setBorder(
                                BorderFactory.createEmptyBorder(10, 12, 10, 12));

                // Painel de pesquisa
                JPanel controles_busca = new JPanel(
                                new FlowLayout(FlowLayout.LEFT, 10, 8));

                controles_busca.setBackground(fundo);

                // Painel de botões
                JPanel controles = new JPanel(
                                new FlowLayout(FlowLayout.LEFT, 10, 8));

                controles.setBackground(fundo);

                // Botões
                JButton atualizar = new JButton("Atualizar listagem");
                JButton buscar = new JButton("Buscar por ID");
                JButton mostrarTodos = new JButton("Mostrar todos");
                JButton botaoConsultar = new JButton("Consultar livros");
                JButton botaoBuscarTitulo = new JButton("Buscar por título");
                JButton botaoCapa = new JButton("Selecionar capa");

                // Personalização dos botões
                JButton[] botoes = {
                                atualizar,
                                buscar,
                                mostrarTodos,
                                botaoConsultar,
                                botaoBuscarTitulo
                };

                for (JButton botao : botoes) {

                        botao.setFont(fonteNegrito);
                        botao.setBackground(verde);
                        botao.setForeground(branco);

                        botao.setFocusPainted(false);
                        botao.setOpaque(true);
                        botao.setContentAreaFilled(true);

                        botao.setBorder(
                                        BorderFactory.createCompoundBorder(
                                                        BorderFactory.createLineBorder(
                                                                        new Color(0, 90, 35)),
                                                        BorderFactory.createEmptyBorder(
                                                                        7, 12, 7, 12)));

                        botao.setCursor(
                                        new Cursor(Cursor.HAND_CURSOR));
                }

                // Personalização dos campos de pesquisa
                JTextField[] campos = {
                                campoTitulo,
                                campoId
                };

                for (JTextField campo : campos) {

                        campo.setFont(fontePadrao);
                        campo.setBackground(corCampo);
                        campo.setForeground(branco);
                        campo.setCaretColor(branco);

                        campo.setBorder(
                                        BorderFactory.createCompoundBorder(
                                                        BorderFactory.createLineBorder(
                                                                        new Color(0, 130, 50), 1),
                                                        BorderFactory.createEmptyBorder(
                                                                        5, 7, 5, 7)));

                        campo.setPreferredSize(
                                        new Dimension(190, 34));
                }

                campoId.setPreferredSize(
                                new Dimension(100, 34));

                // Rótulos dos campos
                JLabel rotuloTitulo = new JLabel("Título:");
                JLabel rotuloId = new JLabel("ID do livro:");

                JLabel[] rotulos = {
                                rotuloTitulo,
                                rotuloId
                };

                for (JLabel rotulo : rotulos) {

                        rotulo.setFont(fonteNegrito);
                        rotulo.setForeground(branco);
                }

                // Primeira linha: pesquisas
                controles_busca.add(rotuloTitulo);
                controles_busca.add(campoTitulo);
                controles_busca.add(botaoBuscarTitulo);

                controles_busca.add(rotuloId);
                controles_busca.add(campoId);
                controles_busca.add(buscar);

                // Segunda linha: ações
                controles.add(atualizar);
                controles.add(mostrarTodos);
                controles.add(botaoConsultar);
                controles.add(botaoCapa);

                painelSuperior.add(controles_busca);
                painelSuperior.add(controles);

                // Barra inferior de status
                status.setFont(fonteNegrito);
                status.setForeground(branco);
                status.setBackground(fundo);
                status.setOpaque(true);

                status.setBorder(
                                BorderFactory.createEmptyBorder(
                                                8, 10, 8, 10));

                // Área de rolagem
                JScrollPane scroll = new JScrollPane(tabela);

                scroll.setBorder(
                                BorderFactory.createLineBorder(
                                                new Color(160, 170, 165)));

                scroll.getViewport().setBackground(fundo);

                // Adicionar componentes à janela
                add(painelSuperior, BorderLayout.NORTH);
                add(scroll, BorderLayout.CENTER);
                add(status, BorderLayout.SOUTH);

                // Eventos dos botões
                atualizar.addActionListener(
                                e -> carregarLivros());

                mostrarTodos.addActionListener(
                                e -> carregarLivros());

                buscar.addActionListener(
                                e -> buscarLivro());

                botaoConsultar.addActionListener(e -> {
                        new TelaLivros().setVisible(true);});

                botaoBuscarTitulo.addActionListener(
                                e -> buscarPorTitulo());

                botaoCapa.addActionListener(
                                e -> selecionarCapa());

                campoTitulo.addActionListener(
                                e -> buscarPorTitulo());

                campoId.addActionListener(
                                e -> buscarLivro());

                carregarLivros();
        }

        private void carregarLivros() {

                modelo.setRowCount(0);

                List<Livro> livros = dao.listarLivros();

                for (Livro livro : livros) {
                        adicionarLinha(livro);
                }

                status.setText(
                                "Livros apresentados: " + livros.size());
        }

        private void adicionarLinha(Livro livro) {

                modelo.addRow(new Object[] {
                                livro.getId(),
                                "Sem capa cadastrada",
                                livro.getTitulo(),
                                livro.getAutor(),
                                livro.getAno()
                });
        }

        private void buscarLivro() {

                String texto = campoId.getText().trim();

                int id;

                try {
                        id = Integer.parseInt(texto);

                        if (id <= 0) {
                                throw new NumberFormatException();
                        }

                } catch (NumberFormatException ex) {

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Informe um ID inteiro positivo.",
                                        "Entrada inválida",
                                        JOptionPane.WARNING_MESSAGE);

                        return;
                }

                Livro livro = dao.buscarLivroPorId(id);

                modelo.setRowCount(0);

                if (livro == null) {

                        status.setText(
                                        "Nenhum livro encontrado para o ID " + id);

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Livro não encontrado.");

                } else {

                        adicionarLinha(livro);

                        status.setText(
                                        "Livro encontrado: " + livro.getTitulo());
                }

                campoId.setText("");
        }

        private void buscarPorTitulo() {

                String titulo = campoTitulo.getText().trim();

                if (titulo.isEmpty()) {

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Informe o título do livro.",
                                        "Campo obrigatório",
                                        JOptionPane.WARNING_MESSAGE);

                        return;
                }

                List<Livro> livros = dao.buscarLivrosPorTitulo(titulo);

                modelo.setRowCount(0);

                for (Livro livro : livros) {
                        adicionarLinha(livro);
                }

                status.setText(
                                "Livros encontrados: " + livros.size());

                if (livros.isEmpty()) {

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Nenhum livro encontrado.");
                }

                campoTitulo.setText("");
        }

        private void selecionarCapa() {

                int linha = tabela.getSelectedRow();

                if (linha == -1) {
                        JOptionPane.showMessageDialog(
                                        this,
                                        "Selecione um livro na tabela.");
                        return;
                }

                int linhaModelo = tabela.convertRowIndexToModel(linha);

                int id = (int) modelo.getValueAt(
                                linhaModelo, 0);

                JFileChooser seletor = new JFileChooser();

                seletor.setDialogTitle(
                                "Selecione a capa do livro");

                seletor.setFileFilter(
                                new javax.swing.filechooser.FileNameExtensionFilter(
                                                "Imagens JPG e PNG", "jpg", "jpeg", "png"));

                if (seletor.showOpenDialog(this) != JFileChooser.APPROVE_OPTION) {
                        return;
                }

                java.nio.file.Path destino = null;

                try {

                        destino = java.nio.file.Path.of(
                                        ImagemLivro.salvar(
                                                        seletor.getSelectedFile().toPath(),
                                                        id));

                        boolean atualizado = dao.atualizarCapa(
                                        id, destino.toString().replace('\\', '/'));

                        if (!atualizado) {

                                java.nio.file.Files.deleteIfExists(destino);

                                JOptionPane.showMessageDialog(
                                                this,
                                                "Não foi possível atualizar o livro.");

                                return;
                        }

                        carregarLivros();

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Capa salva com sucesso!");

                } catch (Exception ex) {

                        if (destino != null) {
                                try {
                                        java.nio.file.Files.deleteIfExists(destino);
                                } catch (java.io.IOException ignorado) {
                                }
                        }

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Erro ao salvar capa: " +
                                                        ex.getMessage());
                }
        }

        public static void main(String[] args) {

                SwingUtilities.invokeLater(() -> {
                        new TelaLivros().setVisible(true);
                });
        }
}
