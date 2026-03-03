# =================================================
# SISTEMA DE CONTROLE DE ESTOQUE
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor      : Cauã Borcezi Ferreira
# Data       : 26/02/2026
# Repositório: https://github.com/cborcezi/2026-PS
# =================================================
#
#
# DESCRIÇÃO: 
# Você foi contratado como desenvolvedor júnior por uma
# pequena loja de informática. O gerente precisa de um
# programa simples em Python para controlar o estoque de
# produtos. Ele quer saber quais produtos estão com
# quantidade crítica (menos de 5 unidades), quais estão
# adequados (entre 5 e 20) e quais estão com excesso
# (mais de 20). Seu programa será a primeira entrega do
# projeto.
# =================================================

# Lista inicial de produtos
estoque = [
    {"nome": "Teclado", "quantidade": 3},
    {"nome": "Mouse", "quantidade": 12},
    {"nome": "Monitor", "quantidade": 25},
    {"nome": "Mouse Pad", "quantidade": 9}
]

print("\n=== RELATÓRIO DE ESTOQUE ===")

critico = adequado = excesso = 0

# Relatório principal
for produto in estoque:
    nome = produto["nome"]
    qtd = produto["quantidade"]

    if qtd < 5:
        situacao = "Crítico"
        critico += 1
    elif qtd <= 20:
        situacao = "Adequado"
        adequado += 1
    else:
        situacao = "Excesso"
        excesso += 1

    print(f"{nome} | Quantidade: {qtd} | Situação: {situacao}")

# Resumo
print("\nResumo:")
print(f"Críticos: {critico}")
print(f"Adequados: {adequado}")
print(f"Excesso: {excesso}")

# Consulta de produto
while input("\nDeseja consultar um produto? (s/n): ").lower() == "s":
    busca = input("Nome do produto: ").lower()
    encontrado = False

    for produto in estoque:
        if produto["nome"].lower() == busca:
            qtd = produto["quantidade"]
            if qtd < 5:
                situacao = "Crítico"
            elif qtd <= 20:
                situacao = "Adequado"
            else:
                situacao = "Excesso"

            print(f"{produto['nome']} | Quantidade: {qtd} | Situação: {situacao}")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado.")

# Adicionar novos produtos
while input("\nDeseja adicionar produto? (s/n): ").lower() == "s":
    nome = input("Nome: ")

    while True:
        try:
            qtd = int(input("Quantidade: "))
            if qtd < 0:
                print("Quantidade não pode ser negativa.")
            else:
                break
        except:
            print("Digite um número válido.")

    estoque.append({"nome": nome, "quantidade": qtd})
    print("Produto adicionado.")

# Produto mais crítico
menor = estoque[0]
for produto in estoque:
    if produto["quantidade"] < menor["quantidade"]:
        menor = produto

print("\nProduto com menor estoque:")
print(f"{menor['nome']} | Quantidade: {menor['quantidade']}")

print("\nPrograma finalizado.")