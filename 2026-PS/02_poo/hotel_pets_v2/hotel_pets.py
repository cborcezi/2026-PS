# ===================================================
# Disciplina : Programação de Sistemas
# Aula       : 23 - Menu interativo e persistência de objetos
# Autor      : Cauã Borcezi Ferreira
# Data       : 14/05/2026
# ===================================================

import pickle
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pet import Pet

ARQUIVO_BIN = "2026-PS/02_poo/hotel_pets_v2/pets.bin"
ARQUIVO_TXT = "2026-PS/02_poo/hotel_pets_v2/pets.txt"

# SALVAR PETS EM BINÁRIO
def salvar_pets_binario(pets):
    with open(ARQUIVO_BIN, "wb") as arquivo:
        pickle.dump(pets, arquivo)

# CARREGAR PETS EM BINÁRIO
def carregar_pets():
    if os.path.exists(ARQUIVO_BIN):
        with open(ARQUIVO_BIN, "rb") as arquivo:
            return pickle.load(arquivo)
    return []

# SALVAR PETS EM TXT
def salvar_pets_txt(pets):
    with open(ARQUIVO_TXT, "w", encoding="utf-8") as arquivo:
        for pet in pets:
            linha = (
                f"{pet.nome};"
                f"{pet.especie};"
                f"{pet.idade};"
                f"{pet.raca};"
                f"{pet.peso};"
                f"{pet.porte};"
                f"{pet.dono};"
                f"{pet.vacinado};"
                f"{pet.hospedado}\n"
            )
            arquivo.write(linha)

# CADASTRAR PET
def cadastrar_pet(pets):
    print("\n===== CADASTRO DE PET =====")
    nome = input("Nome: ")
    especie = input("Espécie: ")
    idade = int(input("Idade: "))
    raca = input("Raça: ")
    peso = float(input("Peso: "))
    porte = input("Porte: ")
    dono = input("Nome do(a) dono(a): ")
    vacinado = input("Vacinado? (s/n): ").lower() == "s"
    novo_pet = Pet(
        nome,
        especie,
        idade,
        raca,
        peso,
        porte,
        dono,
        vacinado
    )
    pets.append(novo_pet)
    print("\nPet cadastrado com sucesso!")

# LISTAR PETS
def listar_pets(pets):
    if len(pets) == 0:
        print("\nNenhum pet cadastrado.")
        return
    print("\n===== LISTA DE PETS =====")
    for i, pet in enumerate(pets):
        print(f"\nPET {i + 1}")
        pet.exibir_dados()

# ESCOLHER PET
def escolher_pet(pets):
    if len(pets) == 0:
        print("\nNenhum pet cadastrado.")
        return None
    print("\n===== ESCOLHA UM PET =====")
    for i, pet in enumerate(pets):
        print(f"{i + 1} - {pet.nome}")
    try:
        indice = int(input("\nEscolha o número do pet: ")) - 1
        if 0 <= indice < len(pets):
            return pets[indice]
        print("Pet inválido.")
        return None
    except:
        print("Erro ao selecionar pet.")
        return None

# BUSCAR PET POR NOME
def buscar_pet(pets):
    nome = input("\nDigite o nome do pet: ").lower()
    encontrados = []
    for pet in pets:
        if nome in pet.nome.lower():
            encontrados.append(pet)
    if len(encontrados) == 0:
        print("\nNenhum pet encontrado.")
        return
    for pet in encontrados:
        pet.exibir_dados()

# RELATÓRIO DE HOSPEDAGEM
def relatorio_hospedados(pets):
    total = 0
    encontrou = False
    for pet in pets:
        if pet.hospedado:
            encontrou = True
            pet.emitir_resumo()
            total += pet.calcular_diaria()
    if not encontrou:
        print("\nNenhum pet hospedado.")
    print(f"\nTotal arrecadado no dia: R$ {total:.2f}")

# MENU PRINCIPAL
def main():
    pets = carregar_pets()
    while True:
        print("\n========== HOTEL PET ==========")
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Check-in")
        print("4 - Check-out")
        print("5 - Atualizar peso")
        print("6 - Emitir resumo")
        print("7 - Buscar pet")
        print("8 - Relatório de hospedados")
        print("9 - Salvar em TXT")
        print("10 - Salvar em BINÁRIO")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")
        # CADASTRAR PET
        if opcao == "1":
            cadastrar_pet(pets)
        # LISTAR PETS
        elif opcao == "2":
            listar_pets(pets)
        # CHECK-IN
        elif opcao == "3":
            pet = escolher_pet(pets)
            if pet:
                pet.registrar_entrada()
        # CHECK-OUT
        elif opcao == "4":
            pet = escolher_pet(pets)
            if pet:
                pet.registrar_saida()
        # ATUALIZAR PESO
        elif opcao == "5":
            pet = escolher_pet(pets)
            if pet:
                try:
                    novo_peso = float(input("Novo peso: "))
                    pet.atualizar_peso(novo_peso)
                except:
                    print("Peso inválido.")
        # EMITIR RESUMO
        elif opcao == "6":
            pet = escolher_pet(pets)

            if pet:
                pet.emitir_resumo()
        # BUSCAR PET
        elif opcao == "7":
            buscar_pet(pets)
        # RELATÓRIO
        elif opcao == "8":
            relatorio_hospedados(pets)
        # SALVAR TXT
        elif opcao == "9":
            salvar_pets_txt(pets)
            print("\nPets salvos em TXT!")
        # SALVAR BINÁRIO
        elif opcao == "10":
            salvar_pets_binario(pets)
            print("\nPets salvos em BINÁRIO!")
        # SAIR
        elif opcao == "0":
            salvar_pets_binario(pets)
            salvar_pets_txt(pets)
            print("\nDados salvos com sucesso!")
            print("Encerrando sistema")
            break
        else:
            print("\nOpção inválida.")

# EXECUTAR SISTEMA
main()