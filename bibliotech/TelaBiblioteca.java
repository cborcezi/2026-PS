
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.awt.Color;
import java.awt.Font;
import java.awt.Dimension;
import java.awt.Cursor;
import java.awt.Component;
import javax.swing.*;

public class TelaBiblioteca extends JFrame {

    private Biblioteca biblioteca;
    private JTextField campoTitulo;
    private JTextField campoMatricula;
    private JTextArea areaAcervo;

    // Cores da interface
    private final Color verde = new Color(0, 120, 45);
    private final Color verdeClaro = new Color(0, 150, 55);
    private final Color fundo = new Color(35, 39, 42);
    private final Color grafite = new Color(55, 60, 65);
    private final Color branco = new Color(255, 255, 255);
    private final Color corCampo = new Color(75, 82, 87);

    // Fontes
    private final Font fontePadrao = new Font("Segoe UI", Font.PLAIN, 15);

    private final Font fonteNegrito = new Font("Segoe UI", Font.BOLD, 14);

    private final Font fonteTitulo = new Font("Segoe UI", Font.BOLD, 26);

    private final Font fonteSubtitulo = new Font("Segoe UI", Font.PLAIN, 14);

    public TelaBiblioteca(Biblioteca biblioteca) {

        this.biblioteca = biblioteca;

        // Configuração das fontes padrão
        UIManager.put("OptionPane.messageFont", fontePadrao);
        UIManager.put("OptionPane.buttonFont", fonteNegrito);

        setTitle("BiblioTech");
        setSize(760, 480);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(0, 0));

        getContentPane().setBackground(fundo);

        // Painel superior
        JPanel painelSuperior = new JPanel();

        painelSuperior.setLayout(
                new BoxLayout(painelSuperior, BoxLayout.Y_AXIS));

        painelSuperior.setBackground(fundo);

        painelSuperior.setBorder(
                BorderFactory.createEmptyBorder(15, 15, 15, 15));

        // Título visual centralizado
        JLabel titulo = new JLabel("BiblioTech");

        titulo.setFont(fonteTitulo);
        titulo.setForeground(branco);
        titulo.setAlignmentX(Component.CENTER_ALIGNMENT);

        JLabel subtitulo = new JLabel(
                "Gerenciamento de empréstimos e acervo");

        subtitulo.setFont(fonteSubtitulo);
        subtitulo.setForeground(new Color(190, 195, 195));
        subtitulo.setAlignmentX(Component.CENTER_ALIGNMENT);

        painelSuperior.add(titulo);
        painelSuperior.add(Box.createVerticalStrut(5));
        painelSuperior.add(subtitulo);
        painelSuperior.add(Box.createVerticalStrut(25));

        // Painel dos campos centralizados
        JPanel campos = new JPanel(new GridBagLayout());

        campos.setBackground(fundo);

        GridBagConstraints gbc = new GridBagConstraints();

        gbc.insets = new Insets(5, 8, 5, 8);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        campoTitulo = new JTextField();
        campoMatricula = new JTextField();

        campoTitulo.setPreferredSize(
                new Dimension(300, 34));

        campoMatricula.setPreferredSize(
                new Dimension(300, 34));

        JLabel rotuloTitulo = new JLabel("Título do livro:");
        JLabel rotuloMatricula = new JLabel("Matrícula do leitor:");

        JLabel[] rotulos = {
                rotuloTitulo,
                rotuloMatricula
        };

        for (JLabel rotulo : rotulos) {

            rotulo.setFont(fonteNegrito);
            rotulo.setForeground(branco);
        }

        // Personalização dos campos
        JTextField[] camposTexto = {
                campoTitulo,
                campoMatricula
        };

        for (JTextField campo : camposTexto) {

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
        }

        // Primeira linha
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.EAST;

        campos.add(rotuloTitulo, gbc);

        gbc.gridx = 1;
        gbc.anchor = GridBagConstraints.WEST;

        campos.add(campoTitulo, gbc);

        // Segunda linha
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.EAST;

        campos.add(rotuloMatricula, gbc);

        gbc.gridx = 1;
        gbc.anchor = GridBagConstraints.WEST;

        campos.add(campoMatricula, gbc);

        campos.setAlignmentX(Component.CENTER_ALIGNMENT);

        painelSuperior.add(campos);

        add(painelSuperior, BorderLayout.NORTH);

        // Área do acervo
        areaAcervo = new JTextArea();

        areaAcervo.setEditable(false);
        areaAcervo.setLineWrap(true);
        areaAcervo.setWrapStyleWord(true);

        areaAcervo.setFont(fontePadrao);
        areaAcervo.setBackground(grafite);
        areaAcervo.setForeground(branco);
        areaAcervo.setCaretColor(branco);

        areaAcervo.setBorder(
                BorderFactory.createEmptyBorder(
                        10, 10, 10, 10));

        JScrollPane scroll = new JScrollPane(areaAcervo);

        scroll.setBorder(
                BorderFactory.createLineBorder(
                        new Color(160, 170, 165)));

        scroll.getViewport().setBackground(grafite);

        add(scroll, BorderLayout.CENTER);

        // Painel dos botões
        JPanel botoes = new JPanel(
                new FlowLayout(FlowLayout.CENTER, 12, 12));

        botoes.setBackground(fundo);

        botoes.setBorder(
                BorderFactory.createEmptyBorder(0, 10, 5, 10));

        JButton botaoEmprestar = new JButton("Emprestar");
        JButton botaoDevolver = new JButton("Devolver");
        JButton botaoAtualizar = new JButton("Atualizar acervo");

        // Personalização dos botões
        JButton[] listaBotoes = {
                botaoEmprestar,
                botaoDevolver,
                botaoAtualizar
        };

        for (JButton botao : listaBotoes) {

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
                                    7, 15, 7, 15)));

            botao.setCursor(
                    new Cursor(Cursor.HAND_CURSOR));
        }

        botoes.add(botaoEmprestar);
        botoes.add(botaoDevolver);
        botoes.add(botaoAtualizar);

        add(botoes, BorderLayout.SOUTH);

        // Eventos dos botões
        botaoEmprestar.addActionListener(e -> emprestar());
        botaoDevolver.addActionListener(e -> devolver());
        botaoAtualizar.addActionListener(e -> atualizarAcervo());

        atualizarAcervo();
    }

    private void atualizarAcervo() {

        areaAcervo.setText(
                biblioteca.obterAcervoComoTexto());

        areaAcervo.setCaretPosition(0);
    }

    private void emprestar() {

        String titulo = campoTitulo.getText().trim();
        String matricula = campoMatricula.getText().trim();

        if (titulo.isEmpty() || matricula.isEmpty()) {

            JOptionPane.showMessageDialog(
                    this,
                    "Preencha o título e a matrícula.");

            return;
        }

        boolean resultado = biblioteca.emprestar(titulo, matricula);

        atualizarAcervo();

        if (resultado) {

            JOptionPane.showMessageDialog(
                    this,
                    "Empréstimo realizado.");

        } else {

            JOptionPane.showMessageDialog(
                    this,
                    "Empréstimo recusado. Confira o título, a matrícula, "
                            + "a disponibilidade e o limite do leitor.");
        }
    }

    private void devolver() {

        String titulo = campoTitulo.getText().trim();

        if (titulo.isEmpty()) {

            JOptionPane.showMessageDialog(
                    this,
                    "Preencha o título do livro.");

            return;
        }

        boolean resultado = biblioteca.devolver(titulo);

        atualizarAcervo();

        if (resultado) {

            JOptionPane.showMessageDialog(
                    this,
                    "Devolução registrada.");

        } else {

            JOptionPane.showMessageDialog(
                    this,
                    "Nenhum empréstimo ativo encontrado para esse título.");
        }
    }

    public boolean atualizarFotoUsuario(
            int id, String caminho) {

        String sql = "UPDATE usuarios SET foto = ? WHERE id = ?";

        try (
                Connection conexao = Conexao.conectar();
                PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, caminho);
            comando.setInt(2, id);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {

            System.out.println(e.getMessage());
            return false;
        }
    }

    public static void main(String[] args) {

        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarLivro(
                new Livro("Dom Casmurro", "Machado de Assis", 1899));

        biblioteca.cadastrarLivro(
                new Livro("Capitaes da Areia", "Jorge Amado", 1937));

        biblioteca.cadastrarLeitor(
                new Leitor("Pedro Alves", "2026010", 1));

        biblioteca.cadastrarLeitor(
                new Leitor("Ana Lima", "2026011", 2));

        SwingUtilities.invokeLater(() -> {

            TelaBiblioteca tela = new TelaBiblioteca(biblioteca);
            tela.setVisible(true);

        });
    }
}
