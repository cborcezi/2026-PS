# =================================================
# SISTEMA DE BIBLIOTECA
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05: Revisão: Estruturas de Dados (Listas e Dicionários)
# Autor      : Cauã Borcezi Ferreira
# Data       : 03/03/2026
# Repositório: https://github.com/cborcezi/2026-PS
# =================================================
#
#
# DESCRIÇÃO:
# Você foi contratado como desenvolvedor júnior por uma
# pequena biblioteca que precisa organizar seu catálogo
# de livros em Python. O sistema deve permitir cadastrar
# novos livros, buscar por autor e controlar empréstimos
# e devoluções, mostrando quais estão disponíveis e
# quais estão emprestados ao final.
# =================================================

# CATÁLOGO INICIAL
catalogo = [
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016, "disponivel": True},
    {"titulo": "Python Fluente", "autor": "Luciano Ramalho", "ano": 2015, "disponivel": False}
]


# MOSTRAR CATÁLOGO
print("\n=== Catálogo da Biblioteca ===\n")

for livro in catalogo:
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print(livro["titulo"], "-", livro["autor"], "-", status)


# CADASTRO DE LIVROS
while True:
    opcao = input("\nDeseja cadastrar um novo livro? (s/n): ").lower()

    if opcao == "s":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))

        novo = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "disponivel": True
        }

        catalogo.append(novo)
        print("Livro cadastrado com sucesso!")

    elif opcao == "n":
        break
    else:
        print("Opção inválida.")


# BUSCA POR AUTOR
print("\n=== Buscar por autor ===")

busca = input("Digite o nome do autor: ").lower()
achou = False

for livro in catalogo:
    if busca in livro["autor"].lower():
        print("Encontrado:", livro["titulo"])
        achou = True

if not achou:
    print("Nenhum livro encontrado.")


# EMPRÉSTIMO / DEVOLUÇÃO
print("\n=== Empréstimo ou devolução ===")

titulo_busca = input("Digite o título do livro: ").lower()
encontrado = False

for livro in catalogo:
    if titulo_busca == livro["titulo"].lower():
        livro["disponivel"] = not livro["disponivel"]
        encontrado = True

        if livro["disponivel"]:
            print("Livro devolvido.")
        else:
            print("Livro emprestado.")
        break

if not encontrado:
    print("Livro não encontrado.")


# RELATÓRIO FINAL
print("\n=== Relatório Final ===")

total = len(catalogo)
disp = 0
emp = 0

print("\nLivros emprestados:")

for livro in catalogo:
    if livro["disponivel"]:
        disp += 1
    else:
        emp += 1
        print("-", livro["titulo"])

print("\nTotal:", total)
print("Disponíveis:", disp)
print("Emprestados:", emp)