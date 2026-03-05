# =================================================
# SISTEMA DE BIBLIOTECA
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados (Listas e Dicionários)
# Autor      : Cauã Borcezi Ferreira
# Data       : 26/02/2026
# Repositório: https://github.com/cborcezi/2026-PS
# =================================================
#
# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.
# =================================================


# -------------------------------------------------
# DICIONÁRIO: EXEMPLO BÁSICO
# -------------------------------------------------

livro_exemplo = {
    "titulo": "O Programador Pragmático",
    "autor": "Andrew Hunt",
    "ano": 1999,
    "disponivel": True,
}

print("Título : ", livro_exemplo["titulo"])
print("Autor  : ", livro_exemplo["autor"])
print("Ano    : ", livro_exemplo["ano"])
print("Status : ", "Disponível" if livro_exemplo["disponivel"] else "Emprestado")


# Atualizando disponibilidade
livro_exemplo["disponivel"] = False
print("\nApós empréstimo:", livro_exemplo["disponivel"])

# Adicionando nova informação
livro_exemplo["paginas"] = 352
print("Páginas:", livro_exemplo["paginas"])

editora = livro_exemplo.get("editora", "Não informada")
print("Editora:", editora)


# -------------------------------------------------
# CATÁLOGO: LISTA DE DICIONÁRIOS
# -------------------------------------------------

catalogo = [
    {
        "titulo": "O Programador Pragmático",
        "autor": "Andrew Hunt",
        "ano": 1999,
        "disponivel": True
    },
    {
        "titulo": "Código Limpo",
        "autor": "Robert C. Martin",
        "ano": 2008,
        "disponivel": False
    },
    {
        "titulo": "Entendendo Algoritmos",
        "autor": "Aditya Bhargava",
        "ano": 2016,
        "disponivel": True
    },
    {
        "titulo": "Introdução à linguagem Python",
        "autor": "Sergio Vicente Denser Pamboukian, "
                 "Lincoln César Zamboni, "
                 "Edson de Almeida Rego Barros",
        "ano": 2020,
        "disponivel": True
    }
]

print("\n=== Catálogo da Biblioteca ===\n")

for numero, item in enumerate(catalogo, start=1):
    status = "Disponível" if item["disponivel"] else "Emprestado"

    print(f'{numero}. {item["titulo"]} ({item["ano"]})')
    print(f'   Autor: {item["autor"]} | {status}')
    print(" " + "-" * 40)


# -------------------------------------------------
# FILTRO: LIVROS DISPONÍVEIS
# -------------------------------------------------

print("\n=== Livros disponíveis ===")
for item in catalogo:
    if item["disponivel"]:
        print(f' {item["titulo"]}')


# -------------------------------------------------
# BUSCA POR TÍTULO
# -------------------------------------------------

print("\n=== Busca por título ===")
busca = input("Digite o título (ou parte): ").lower()

encontrado = False

for item in catalogo:
    if busca in item["titulo"].lower():
        print(f'  Encontrado: {item["titulo"]} — {item["autor"]}')
        encontrado = True

if not encontrado:
    print("  Nenhum livro encontrado com esse termo.")


# -------------------------------------------------
# EXIBIR ATRIBUTOS DO PRIMEIRO LIVRO
# -------------------------------------------------

print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items():
    print(f"  {chave}: {valor}")


# -------------------------------------------------
# CONTADOR DE STATUS
# -------------------------------------------------

print("\n=== Quantidade de livros ===")

disponiveis = 0
emprestados = 0

for item in catalogo:
    if item["disponivel"]:
        disponiveis += 1
    else:
        emprestados += 1

print(f"Disponíveis: {disponiveis} | Emprestados: {emprestados}")