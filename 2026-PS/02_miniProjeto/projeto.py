# =================================================
# SISTEMA DO IF`Donalds
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 12 e 13 - Mini Projeto
# Autor      : Átila, Cauã e Gabriele
# Data       : 07/04/2026
# Descrição  : Sistema de lanchonete que lê o cardápio de um arquivo, permite buscar
#              produtos, realizar compras com atualização de estoque e registra as
#              vendas e relatórios em arquivos .txt.
# =================================================

from datetime import datetime
import os

# PASTA DO ARQUIVO
pasta = os.path.dirname(__file__)
caminho_cardapio = os.path.join(pasta, "cardapio.txt")
caminho_dados = os.path.join(pasta, "dados.txt")
caminho_relatorio = os.path.join(pasta, "relatorio.txt")

# COMPROVA QUE OS ARQUIVOS EXISTEM
open(caminho_dados, "a").close()
open(caminho_relatorio, "a").close()

# CARREGAR O ESTOQUE
def carregar_estoque():
    estoque = {}
    try:
        with open (caminho_cardapio, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) !=4:
                    continue
                categoria = dados [0]
                nome = dados[1]
                preco = float(dados[2])
                qtd = int(dados[3])
                if categoria not in estoque:
                    estoque[categoria] = []
                estoque[categoria].append({
                    "nome": nome,
                    "preco": preco,
                    "qtd": qtd
                })
    except:
        print("Erro ao abrir o cardápio")
    return estoque

# SALVAR ESTOQUE
def salvar_estoque(estoque):
    with open(caminho_cardapio, "w", encoding="utf-8") as arquivo:
        for categoria in estoque:
            for produto in estoque[categoria]:
                linha = categoria + ";" + produto["nome"] + ";" + str(produto["preco"]) + ";" + str(produto["qtd"]) + "\n"
                arquivo.write(linha)

# HISTÓRICO
def salvar_historico(texto):
    with open(caminho_dados, "a", encoding="utf-8") as arq:
        arq.write(texto+"\n")

# RELATÓRIO
def salvar_relatorio(total_itens, total_valor, media, maior, menor):
    with open(caminho_relatorio, "w", encoding="utf-8") as arq:
        arq.write("Relatório Estatístico do Estoque\n")
        arq.write("Itens: " + str(total_itens) + "\n")
        arq.write("Valor total: R$ " + "%.2f" % total_valor + "\n")
        arq.write("Média: R$ " + "%.2f" % media + "\n")
        arq.write("Maior: R$ " + "%.2f" % maior + "\n")
        arq.write("Menor: R$ " + "%.2f" % menor + "\n")
        arq.write("-------------------------")
    
# VER PRODUTOS
def ver_produtos(estoque):
    categorias = list(estoque.keys())
    while True:
        print("\n--- CATEGORIAS ---")
        for i in range(len(categorias)):
            print(i+1, "-", categorias[i])
        print("0 - Voltar")
        op = input("\nEscolha: ")
        if op=="0":
            return
        if not op.isdigit():
            print("Opção Inválida")
            continue
        op = int(op)
        if op < 1 or op > len(categorias):
            print("Opção Inválida")
            continue
        categoria = categorias[op-1]
        print("\n---", categoria, "---")
        for p in estoque[categoria]:
            print(p["nome"], "- R$", "%.2f" % p["preco"], "(Estoque:", p["qtd"], ")")

# BUSCAR PRODUTO    
def buscar_produto(estoque):
    print("\n1 - Nome")
    print("2 - Categoria")
    print("3 - Preço")
    op = input("\nEscolha: ")
    achou = False
    if op=="1":
        nome = input("Digite o nome: ").lower()
        for cat in estoque:
            for p in estoque[cat]:
                print(cat, "-", p["nome"], "- R$", "%.2f" % p["preco"])
                achou = True
    elif op=="2":
        cat = input("Categoria: ")
        if cat in estoque:
            for p in estoque[cat]:
                print(p["nome"], "-R$", "%.2f" % p["preco"])
                achou = True
    elif op=="3":
        try: 
            minimo = float(input("Min: "))
            maximo = float(input("Max: "))
        except:
            print("Erro")
            return
        for cat in estoque:
            for p in estoque[cat]:
                if minimo <= p["preco"] <= maximo:
                    print(cat, "-", p["nome"], "-R$", "%.2f" % p["preco"])
                    achou = True
    if not achou:
        print("Não encontrado")       
    
# REALIZAR COMPRA
def realizar_compra(estoque):
    carrinho = []
    while True:
        categorias = list(estoque.keys())
        print("\n--- CATEGORIAS ---")
        for i in range(len(categorias)):
            print(i+1, "-", categorias[i])
        print("0 - Finalizar")
        op = input("\nEscolha: ")
        if op == "0":
            break
        if not op.isdigit():
            print("Opção Inválida")
            continue
        op = int(op)
        if op < 1 or op > len(categorias):
            print("Opção Inválida")
            continue
        categoria = categorias[op-1]
        while True:
            produtos = estoque[categoria]
            print("\n---", categoria, "---")
            for i in range(len(produtos)):
                p = produtos[i]
                print(i+1, "-", p["nome"], "- R$", "%.2f" % p["preco"], "(Estoque:", p["qtd"], ")")
            print("0 - Voltar")
            op2 = input("\nEscolha: ")
            if op2 == "0":
                break
            if not op2.isdigit():
                print("Opção Inválida")
                continue
            op2 = int(op2)
            if op2 < 1 or op2 > len(produtos):
                print("Opção Inválida")
                continue
            produto = produtos[op2-1]
            if produto["qtd"] <= 0:
                print("Sem estoque")
                continue
            carrinho.append(produto)
            produto["qtd"] -= 1
            print("Produto adicionado")
    if len(carrinho) == 0:
        print("Carrinho vazio")
        return
    subtotal = 0
    for p in carrinho:
        subtotal += p["preco"]
    print("\n--- PAGAMENTO ---")
    print("Total a pagar: R$", "%.2f" % subtotal)
    while True:
        print("1 - Dinheiro")
        print("2 - Débito")
        print("3 - Crédito")
        op = input("\nEscolha: ")
        if op == "1":
            metodo = "Dinheiro"
            break
        elif op == "2":
            metodo = "Débito"
            break
        elif op == "3":
            metodo = "Crédito"
            break
        else:
            print("Opção Inválida")
    total = subtotal
    if metodo == "Dinheiro":
        print("Valor a pagar: R$", "%.2f" % total)
        while True:
            try:
                pago = float(input("Valor pago: "))
            except:
                print("Erro")
                continue
            if pago < total:
                print("Falta dinheiro")
            else:
                troco = pago - total
                break

    print("\n--- NOTA ---")
    for p in carrinho:
        print(p["nome"], "- R$", "%.2f" % p["preco"])
    print("----------------")
    print("Total: R$", "%.2f" % total)
    if metodo == "Dinheiro":
        print("Troco: R$", "%.2f" % troco)
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    lista = ""
    for p in carrinho:
        lista += p["nome"] + ", "
    lista = lista[:-2]
    texto = "[" + data + "] Compra realizada\n"
    texto += "Método: " + metodo + "\n"
    texto += "Total: R$ " + "%.2f" % total + "\n"
    texto += "Produtos: " + lista + "\n"
    texto += "-------------------------"
    salvar_historico(texto)
    salvar_estoque(estoque)

# RELATÓRIO 
def gerar_relatorio(estoque):
    total_itens=0
    total_valor=0
    maior=0
    menor=0
    for cat in estoque:
        for p in estoque[cat]:
            total_itens+=p["qtd"]
            total_valor+=p["preco"]*p["qtd"]
            if p["preco"]>maior:
                maior=p["preco"]
            if menor==0 or p["preco"]<menor:
                menor=p["preco"]
    if total_itens>0:
        media=total_valor/total_itens
    else:
        media=0

    print("\n--- RELATÓRIO ---")
    print("Itens:", total_itens)
    print("Valor total: R$", "%.2f" % total_valor)
    print("Média: R$", "%.2f" % media)
    print("Maior:", "%.2f" % maior)
    print("Menor:", "%.2f" % menor)
    salvar_relatorio(total_itens, total_valor, media, maior, menor)

# MENU PRINCIPAL
def main():
    estoque=carregar_estoque()
    while True:
        print("\n--- IF DONALDS ---")
        print("1 - Ver cardápio")
        print("2 - Buscar produto")
        print("3 - Comprar")
        print("4 - Relatório")
        print("0 - Sair")
        op=input("\nEscolha: ")
        if op=="1":
            ver_produtos(estoque)
        elif op=="2":
            buscar_produto(estoque)
        elif op=="3":
            realizar_compra(estoque)
        elif op=="4":
            gerar_relatorio(estoque)
        elif op=="0":
            print("Encerrando programa")
            break
        else:
            print("Opção Inválida")

# EXECUTAR
main()