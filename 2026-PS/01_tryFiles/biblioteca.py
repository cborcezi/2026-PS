ARQUIVO = "biblioteca.txt"
SEPARADOR = "|"
ARQUIVO_HISTORICO = "historico.txt"

from datetime import datetime
from zoneinfo import ZoneInfo


def carregar_catalogo():
    catalogo = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo": titulo,
                    "autor": autor,
                    "disponivel": disponivel_str == "True"
                })
    except FileNotFoundError:
        pass
    return catalogo


def salvar_catalogo(catalogo):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for livro in catalogo:
            linha = SEPARADOR.join([
                livro["titulo"],
                livro["autor"],
                str(livro["disponivel"])
            ])
            f.write(linha + "\n")


# Histórico
def registrar_historico(acao, descricao):
    data_hora = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M")
    with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as f:
        f.write(f"{data_hora} - {acao}: {descricao}\n")


def ver_historico():
    print("\nHISTÓRICO DE OPERAÇÕES")
    print("=" * 50)
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
            if not conteudo:
                print("Nenhum histórico registrado.")
            else:
                print(conteudo)
    except FileNotFoundError:
        print("Nenhum histórico encontrado.")
    print("=" * 50)


# Relatório (Nível A)
def relatorio_acervo(catalogo):
    print("\nRELATÓRIO DO ACERVO")
    print("=" * 50)

    total = len(catalogo)
    disponiveis = sum(1 for l in catalogo if l["disponivel"])
    emprestados = total - disponiveis

    print(f"Total de livros      : {total}")
    print(f"Disponíveis          : {disponiveis}")
    print(f"Emprestados          : {emprestados}")

    contagem = {}

    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            for linha in f:
                if "EMPRÉSTIMO" in linha:
                    titulo = linha.strip().split(": ")[-1]
                    contagem[titulo] = contagem.get(titulo, 0) + 1

        if contagem:
            mais_emprestado = max(contagem, key=contagem.get)
            print(f"\n📚 Livro mais emprestado: {mais_emprestado}")
            print(f"Quantidade de empréstimos: {contagem[mais_emprestado]}")
        else:
            print("\nNenhum empréstimo registrado ainda.")

    except FileNotFoundError:
        print("\nHistórico não encontrado.")

    print("=" * 50)

# Funcionalidades
def listar_livros(catalogo):
    print("\n" + "=" * 50)
    print("CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)
    if not catalogo:
        print("  Nenhum livro cadastrado.")
        return
    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
        print(f"  {i}. {livro['titulo']} – {livro['autor']}  [{status}]")
    print("=" * 50)


def adicionar_livro(catalogo):
    print("\n--- Adicionar Novo Livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor : ").strip()

    if not titulo or not autor:
        print("Título e autor são obrigatórios.")
        return

    # validação de duplicatas (Nível A)
    for livro in catalogo:
        if livro["titulo"].lower() == titulo.lower():
            print("⚠️ Livro já cadastrado.")
            return

    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })

    salvar_catalogo(catalogo)

    # registro no histórico
    registrar_historico("CADASTRO", f"{titulo} | {autor}")

    print(f"✅ '{titulo}' adicionado com sucesso!")


def buscar_livro(catalogo):
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()
    resultados = [l for l in catalogo if termo in l["titulo"].lower()]

    if not resultados:
        print("  Nenhum livro encontrado.")
        return

    print(f"\n  {len(resultados)} resultado(s):")
    for livro in resultados:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"  • {livro['titulo']} — {livro['autor']}  [{status}]")


def registrar_emprestimo(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return

    print("\n--- Registrar Empréstimo ---")

    try:
        numero = int(input("Número do livro: "))

        if numero < 1 or numero > len(catalogo):
            print("Número fora do intervalo.")
            return

        livro = catalogo[numero - 1]

        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            salvar_catalogo(catalogo)
            registrar_historico("EMPRÉSTIMO", livro["titulo"])
            print(f"Empréstimo de '{livro['titulo']}' registrado.")

    except ValueError:
        print("Entrada inválida. Digite apenas o número.")


def devolver_livro(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return

    print("\n--- Registrar Devolução ---")

    try:
        numero = int(input("Número do livro a devolver: "))

        if numero < 1 or numero > len(catalogo):
            print("Número fora do intervalo.")
            return

        livro = catalogo[numero - 1]

        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            salvar_catalogo(catalogo)
            registrar_historico("DEVOLUÇÃO", livro["titulo"])
            print(f"Devolução de '{livro['titulo']}' registrada.")

    except ValueError:
        print("Digite apenas o número do livro.")
    except IndexError:
        print("Número fora da lista.")

# Menu
def menu():
    catalogo = carregar_catalogo()
    total = len(catalogo)

    print(f"\n SISTEMA DE BIBLIOTECA — v3 (Nível A completo)")
    print(f"    {total} livro(s) carregado(s) de '{ARQUIVO}'.")

    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", buscar_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Devolver livro", devolver_livro),
        "6": ("Ver histórico", lambda _: ver_historico()),
        "7": ("Relatório de acervo", relatorio_acervo),
        "0": ("Sair", None),
    }

    while True:
        print("\n Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")

        try:
            escolha = input("\n Sua escolha: ").strip()

            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")

        except ValueError as e:
            print(f"{e}")
            continue

        else:
            if escolha == "0":
                print("\n Até logo!")
                break

            _, funcao = opcoes[escolha]
            funcao(catalogo)

if __name__ == "__main__":
    menu()