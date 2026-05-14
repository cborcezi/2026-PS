# ===================================================
# Disciplina : Programação de Sistemas
# Aula       : 23 - Menu interativo e persistência de objetos
# Autor      : Cauã Borcezi Ferreira
# Data       : 07/05/2026
# Descrição  : Agenda de Contatos com menu, CRUD em memória
#              e dois formatos de persistência (.txt e binário).
#              Serve de modelo para o Sistema de Hotel para Pets V2.0
# ===================================================

import pickle   # módulo padrão do Python para "serializar" objetos

class Contato:
    """ Representa um contato simples na agenda."""

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print(f"    Nome    : {self.nome}")
        print(f"    Telefone: {self.telefone}")
        print(f"    Email   : {self.email}")
    
    def para_linha_txt(self):
        return f"{self.nome};{self.telefone};{self.email}"
    
def salvar_em_txt(contatos, caminho):
    """Grava cada contato como uma linha no arquivo de texto."""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in contatos:
            arquivo.write(c.para_linha_txt() + "\n")
    print(f"✓ {len(contatos)} contato(s) salvo(s) em {caminho}")

def carregar_de_txt(caminho):
    """Lê o arquivo de texto e RECONSTRÓI os objetos Contato."""
    contatos = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                nome, telefone, email = partes[0], partes[1], partes[2]
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
    return contatos


# ===================================================
# PERSISTÊNCIA BINÁRIA (pickle)
# ===================================================

def salvar_em_binario(contatos, caminho):
    """Serializa a lista inteira de contatos em formato binário."""
    with open(caminho, "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print(f"✓ {len(contatos)} contato(s) salvo(s) em {caminho}")

def carregar_de_binario(caminho):
    """Lê o arquivo binário e devolve a lista de objetos pronta."""
    try: 
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
        return []
    

# ===================================================
# CRUD EM MEMÓRIA
# ===================================================
def cadastrar(contatos):
    """Lê os dados via inpurt e adiciona um novo Contato na lista."""
    print("\n--- Novo contato ---")
    nome = input("Nome  : ")
    telefone = input("Telefone: ")
    email=input("Email  : ")
    contatos.append(Contato(nome, telefone, email))
    print("✓ Contato cadastrado.")

def listar(contatos):
    """Mostra todos os contatos cadastrados, numerados."""
    if not contatos:
        print("\n(agenda vazia)")
        return
    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]")
        c.exibir()

def remover(contatos):
    """Mostra a lista, pede um número e remove o contato escolhido."""
    listar(contatos)
    if not contatos:
        return
    indice = int(input("\nNº do contato a remover: ")) - 1
    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"√ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")

# ======================================================
# MENU PRINCIPAL – o "loop de eventos" do programa
# ======================================================
def menu():
    contatos = carregar_de_binario("agenda.bin")
    while True:  # loop infinito – só sai com break (opção 0).
        print("\n========= AGENDA =========")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Salvar em .txt")
        print("5 - Salvar em binário")
        print("0 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            cadastrar(contatos)
        elif opcao == "2":
            listar(contatos)
        elif opcao == "3":
            remover(contatos)
        elif opcao == "4":
            salvar_em_txt(contatos, "2026-PS/02_poo/agenda/agenda.txt")
        elif opcao == "5":
            salvar_em_binario(contatos, "2026-PS/02_poo/agenda/agenda.bin")
        elif opcao == "0":
            salvar_em_binario(contatos, "2026-PS/02_poo/agenda/agenda.bin")
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

# ======================================================
# PONTO DE ENTRADA
# ======================================================
if __name__ == "__main__":
    menu()