# ===================================================
# Disciplina : Programação de Sistemas
# Aula       : 23 - Menu interativo e persistência de objetos
# Autor      : Cauã Borcezi Ferreira
# Data       : 28/05/2026
# ===================================================

import json
import os

ARQUIVO_JSON = "2026-PS/02_poo/hotel_pets_json/pets.json"


class Pet:
    def __init__(self, nome, especie, idade, peso, nome_dono, vacinado, hospedado=False, altura=None, data_nascimento=None):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.nome_dono = nome_dono
        self.vacinado = vacinado
        self.hospedado = hospedado
        self.altura = altura
        self.data_nascimento = data_nascimento

    def exibir_dados(self):
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} kg")
        print(f"Dono: {self.nome_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        print(f"Altura: {self.altura if self.altura is not None else 'Não informado'}")
        print(f"Data de Nascimento: {self.data_nascimento if self.data_nascimento else 'Não informado'}")

    def registrar_entrada(self):
        if self.hospedado:
            print(f"{self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registrar_saida(self):
        if not self.hospedado:
            print(f"{self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")

    def para_dicionario(self):
        """
        Transforma o objeto Pet em um dicionário.

        Isso é necessário porque o JSON não salva diretamente objetos Python.
        Ele salva dados simples: textos, números, booleanos, listas e dicionários.
        """
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "peso": self.peso,
            "nome_dono": self.nome_dono,
            "vacinado": self.vacinado,
            "hospedado": self.hospedado,
            "altura": self.altura,
            "data_nascimento": self.data_nascimento
        }

    @staticmethod
    def criar_de_dicionario(dados):
        """
        Cria um objeto Pet a partir de um dicionário carregado do JSON.
        """
        return Pet(
            dados["nome"],
            dados["especie"],
            dados["idade"],
            dados["peso"],
            dados["nome_dono"],
            dados["vacinado"],
            dados["hospedado"],
            dados.get("altura"),
            dados.get("data_nascimento")
        )


def salvar_pets(lista_pets):
    """
    Salva a lista de objetos Pet no arquivo pets.json.
    """

    lista_dicionarios = []

    for pet in lista_pets:
        lista_dicionarios.append(pet.para_dicionario())

    os.makedirs(os.path.dirname(ARQUIVO_JSON), exist_ok=True)

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)

    print("Dados salvos com sucesso em pets.json!")


def carregar_pets():
    """
    Carrega os pets do arquivo pets.json.

    Se o arquivo ainda não existir, retorna uma lista vazia.
    """

    if not os.path.exists(ARQUIVO_JSON):
        return []

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        lista_dicionarios = json.load(arquivo)

    lista_pets = []

    for dados in lista_dicionarios:
        pet = Pet.criar_de_dicionario(dados)
        lista_pets.append(pet)

    return lista_pets


def cadastrar_pet(lista_pets):
    print("\n--- Cadastro de Pet ---")

    nome = input("Nome do pet: ")
    especie = input("Espécie: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    nome_dono = input("Nome do dono: ")

    resposta = input("O pet está vacinado? (s/n): ").lower()
    vacinado = resposta == "s"

    altura = input("Altura do pet (em metros): ")
    data_nascimento = input("Data de nascimento do pet (DD/MM/AAAA): ")

    pet = Pet(nome, especie, idade, peso, nome_dono, vacinado, altura=altura, data_nascimento=data_nascimento)
    lista_pets.append(pet)

    print("Pet cadastrado com sucesso!")


def listar_pets(lista_pets):
    print("\n--- Lista de Pets ---")

    if not lista_pets:
        print("Nenhum pet cadastrado.")
        return

    for i, pet in enumerate(lista_pets, 1):
        print(f"\nPet {i}:")
        pet.exibir_dados()


def menu():
    pets = carregar_pets()

    while True:
        print("\n========= HOTEL PARA PETS =========")
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Salvar dados")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pet(pets)

        elif opcao == "2":
            listar_pets(pets)

        elif opcao == "3":
            listar_pets(pets)
            numero = int(input("Número do pet: "))
            pets[numero - 1].registrar_entrada()

        elif opcao == "4":
            listar_pets(pets)
            numero = int(input("Número do pet: "))
            pets[numero - 1].registrar_saida()

        elif opcao == "5":
            salvar_pets(pets)

        elif opcao == "0":
            salvar_pets(pets)
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()