# =================================================
# SISTEMA DO MERCADO IF
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 12 e 13- Mini Projeto
# Autor      : Átila, Cauã e Gabriele
# Data       : 28/03/2026
# Repositório: https://github.com/cborcezi/2026-PS
# Descrição  : Sistema de mercado com cadastro de produtos,
#              busca, realização de compras, histórico de operações
#              e relatório estatístico atualizado automaticamente.
# =================================================

from datetime import datetime
import os

# CARREGAR ESTOQUE
def carregar_estoque():
    estoque = {}
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_dados = os.path.join(pasta_atual, "dados.txt")

    if not os.path.exists(caminho_dados):
        open(caminho_dados, "w", encoding="utf-8").close()

    with open(caminho_dados, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            dados = linha.replace("\r", "").split(";")
            if len(dados) != 4:
                continue
            categoria, nome, preco_str, qtd_str = [d.strip() for d in dados]
            try:
                preco = float(preco_str.replace(",", "."))
                qtd = int(qtd_str)
            except ValueError:
                continue
            if categoria not in estoque:
                estoque[categoria] = []
            estoque[categoria].append({"nome": nome, "preco": preco, "qtd": qtd})
    return estoque

# SALVAR ESTOQUE
def salvar_estoque(estoque):
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_dados = os.path.join(pasta_atual, "dados.txt")
    with open(caminho_dados, "w", encoding="utf-8") as arquivo:
        for categoria in estoque:
            for produto in estoque[categoria]:
                arquivo.write(f"{categoria};{produto['nome']};{produto['preco']};{produto['qtd']}\n")
    gerar_relatorio(estoque)  # Atualiza relatório a cada alteração

def salvar_historico(texto):
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_historico = os.path.join(pasta_atual, "historico.txt")
    with open(caminho_historico, "a", encoding="utf-8") as arq:
        arq.write(texto + "\n")

# CADASTRAR PRODUTO
def cadastrar_produto(estoque):
    categorias = list(estoque.keys())
    while True:
        print("\n----- CATEGORIAS -----")
        for i in range(len(categorias)):
            print(f"{i+1} - {categorias[i]}")
        print("0 - Voltar")
        op = input("\nEscolha: ")
        if op == "0":
            return
        if not op.isdigit() or int(op) < 1 or int(op) > len(categorias):
            print("Opção inválida")
            continue
        categoria = categorias[int(op)-1]
        nome = input("\nNome do produto: ").strip()
        # Validação de produto duplicado
        nomes_existentes = [p["nome"].lower() for p in estoque[categoria]]
        if nome.lower() in nomes_existentes:
            print("Produto já existe nessa categoria!")
            continue
        try:
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
        except:
            print("Valor inválido")
            continue

        estoque[categoria].append({"nome": nome, "preco": preco, "qtd": qtd})
        estoque[categoria].sort(key=lambda p: p["nome"].lower())
        salvar_estoque(estoque)

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        registro = (
            f"[{data}] Produto cadastrado\n"
            f"Nome: {nome}\n"
            f"Preço: R$ {preco:.2f}\n"
            f"Quantidade: {qtd}\n"
            f"Categoria: {categoria}\n"
            "-------------------------"
        )
        salvar_historico(registro)
        print("Produto cadastrado!")
        return

# VER PRODUTOS
def ver_produtos(estoque):
    categorias = list(estoque.keys())
    while True:
        print("\n----- CATEGORIAS -----")
        for i in range(len(categorias)):
            print(f"{i+1} - {categorias[i]}")
        print("0 - Voltar")
        op = input("\nEscolha: ")
        if op == "0":
            return
        if not op.isdigit() or int(op) < 1 or int(op) > len(categorias):
            print("Opção inválida")
            continue
        categoria = categorias[int(op)-1]
        print(f"\n--- {categoria} ---")
        for p in estoque[categoria]:
            print(f"{p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['qtd']})")

# BUSCAR PRODUTO
def buscar_produto(estoque):
    print("\n----- BUSCAR PRODUTO -----")
    print("1 - Buscar por nome")
    print("2 - Buscar por categoria")
    print("3 - Buscar por faixa de preço")
    op = input("\nEscolha: ")
    resultados = []
    if op == "1":
        termo = input("Digite o nome ou parte do nome: ").lower()
        for cat in estoque:
            for p in estoque[cat]:
                if termo in p["nome"].lower():
                    resultados.append((cat, p))
    elif op == "2":
        termo = input("Digite a categoria: ").strip()
        if termo in estoque:
            for p in estoque[termo]:
                resultados.append((termo, p))
    elif op == "3":
        try:
            min_val = float(input("Preço mínimo: "))
            max_val = float(input("Preço máximo: "))
        except:
            print("Valores inválidos")
            return
        for cat in estoque:
            for p in estoque[cat]:
                if min_val <= p["preco"] <= max_val:
                    resultados.append((cat, p))
    else:
        print("Opção inválida")
        return
    if resultados:
        print("\n----- RESULTADOS -----")
        for cat, p in resultados:
            print(f"[{cat}] {p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['qtd']})")
    else:
        print("Nenhum produto encontrado.")

# REALIZAR COMPRA
def realizar_compra(estoque):
    carrinho = []
    while True:
        categorias = list(estoque.keys())
        print("\n----- CATEGORIAS -----")
        for i in range(len(categorias)):
            print(f"{i+1} - {categorias[i]}")
        print("0 - Finalizar compra")
        op = input("\nEscolha: ")
        if op == "0":
            break
        if not op.isdigit() or int(op) < 1 or int(op) > len(categorias):
            print("Opção inválida")
            continue
        categoria = categorias[int(op)-1]
        while True:
            produtos = estoque[categoria]
            print(f"\n--- {categoria} ---")
            for i in range(len(produtos)):
                p = produtos[i]
                print(f"{i+1} - {p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['qtd']})")
            print("0 - Voltar")
            op2 = input("\nEscolha: ")
            if op2 == "0":
                break
            if not op2.isdigit() or int(op2) < 1 or int(op2) > len(produtos):
                print("Opção inválida")
                continue
            produto = produtos[int(op2)-1]
            if produto["qtd"] <= 0:
                print("Sem estoque")
                continue
            carrinho.append(produto)
            produto["qtd"] -= 1
            print("Adicionado!")

    if not carrinho:
        print("Carrinho vazio")
        return

    subtotal = sum(p["preco"] for p in carrinho)

    print("\n----- Pagamento -----")
    print(f"Total a pagar: R$ {subtotal:.2f}")
    print("1 - Dinheiro (10%)")
    print("2 - Débito (5%)")
    print("3 - Crédito")
    op = input("\nEscolha: ")
    if op == "1":
        metodo = "Dinheiro"
        desconto = subtotal * 0.10
    elif op == "2":
        metodo = "Debito"
        desconto = subtotal * 0.05
    else:
        metodo = "Credito"
        desconto = 0
    total = subtotal - desconto

    troco = 0
    if metodo == "Dinheiro":
        print(f"Valor a pagar: R$ {total:.2f}")
        while True:
            try:
                pago = float(input("Valor pago: "))
            except:
                print("Valor inválido")
                continue
            if pago < total:
                print("Insuficiente")
            else:
                troco = pago - total
                break

    print("\n----- NOTA FISCAL -----")
    for p in carrinho:
        print(f"{p['nome']} - R$ {p['preco']:.2f}")
    print("------------------")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total: R$ {total:.2f}")
    if metodo == "Dinheiro":
        print(f"Troco: R$ {troco:.2f}")

    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    lista_produtos = ", ".join([p["nome"] for p in carrinho])
    registro = (
        f"[{data}] Compra realizada\n"
        f"Método: {metodo}\n"
        f"Total: R$ {total:.2f}\n"
        f"Produtos: {lista_produtos}\n"
        "-------------------------"
    )
    salvar_historico(registro)
    salvar_estoque(estoque)

# GERAR RELATÓRIO ESTATÍSTICO
def gerar_relatorio(estoque):
    total_itens = 0
    total_valor = 0
    maior_preco = 0
    menor_preco = float('inf')
    for cat in estoque:
        for p in estoque[cat]:
            total_itens += p["qtd"]
            total_valor += p["preco"] * p["qtd"]
            if p["preco"] > maior_preco:
                maior_preco = p["preco"]
            if p["preco"] < menor_preco:
                menor_preco = p["preco"]

    media_valor = total_valor / total_itens if total_itens else 0

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_relatorio = os.path.join(pasta_atual, "relatorio.txt")

    with open(caminho_relatorio, "w", encoding="utf-8") as arq:
        arq.write(f"Relatório Estatístico do Estoque\n")
        arq.write(f"Total de itens em estoque: {total_itens}\n")
        arq.write(f"Valor total do estoque: R$ {total_valor:.2f}\n")
        arq.write(f"Preço médio por item: R$ {media_valor:.2f}\n")
        arq.write(f"Maior preço: R$ {maior_preco:.2f}\n")
        arq.write(f"Menor preço: R$ {menor_preco:.2f}\n")

    print("\n----- RELATÓRIO ESTATÍSTICO -----")
    print(f"Total de itens em estoque: {total_itens}")
    print(f"Valor total do estoque: R$ {total_valor:.2f}")
    print(f"Preço médio por item: R$ {media_valor:.2f}")
    print(f"Maior preço: R$ {maior_preco:.2f}")
    print(f"Menor preço: R$ {menor_preco:.2f}")
    print("-------------------------------")

# VER RELATÓRIO
def ver_relatorio(estoque):
    gerar_relatorio(estoque)
    input("Pressione Enter para voltar ao menu principal...")

# EXECUTAR
def main():
    estoque = carregar_estoque()
    while True:
        print("\n----- SISTEMA DO MERCADO IF -----")
        print("1 - Cadastrar novo produto")
        print("2 - Buscar produto")
        print("3 - Realizar compra")
        print("4 - Ver produtos")
        print("5 - Ver relatório estatístico")
        print("0 - Sair")
        op = input("\nEscolha: ")
        if op == "1":
            cadastrar_produto(estoque)
        elif op == "2":
            buscar_produto(estoque)
        elif op == "3":
            realizar_compra(estoque)
        elif op == "4":
            ver_produtos(estoque)
        elif op == "5":
            ver_relatorio(estoque)
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

main()