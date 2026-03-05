# ============================================
# SISTEMA DE CÁLCULO DE IMC
# ============================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 — Revisão: Funções
# Autor      : Cauã Borcezi Ferreira
# Data       : 05/03/2026
# Repositório: https://github.com/cborcezi/2026-PS.git
# ============================================
# DESCRIÇÃO:
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definição de funções, parâmetros,
# retorno, escopo e recursão.
# ============================================

# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ----
def exibir_cabecalho():
    """Exibe o cabeçalho do sistema no terminal."""
    print("=" * 40)
    print("       SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)


# ---- FUNÇÃO DE RODAPÉ ----
def exibir_rodape():
    """Exibe o rodapé do sistema."""
    print("=" * 40)
    print("Sistema encerrado.")
    print("=" * 40)


# ---- FUNÇÃO COM PARÂMETROS E RETORNO ----
def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura²"""
    imc = peso / (altura ** 2)
    return imc


# ---- ESCOPO LOCAL vs GLOBAL ----
versao = "1.0"   # variável global


def demonstrar_escopo():
    mensagem = "Olá do interior da função"
    print("Dentro da função:")
    print(f" mensagem = {mensagem}")
    print(f" versao = {versao}")


# ---- FUNÇÃO PARA MOSTRAR VERSÃO ----
def mostrar_versao():
    print(f"Sistema IMC — versão {versao}")


# ---- CLASSIFICAÇÃO DO IMC ----
def classificar_imc(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna classificação e emoji."""

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⬇️"
    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "✅"
    elif imc < 30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠️"
    else:
        classificacao = "Obesidade"
        emoji = "🔴"

    return classificacao, emoji


# ---- RECURSÃO BÁSICA ----
def contagem_regressiva(n):
    """Exibe contagem regressiva de n até 0 usando recursão."""
    if n < 0:   # caso base
        return
    print(n)
    contagem_regressiva(n - 1)


# ---- FATORIAL RECURSIVO ----
def fatorial(n):
    """Calcula n! recursivamente."""
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


# ---- SOMA RECURSIVA ----
def soma_regressiva(n):
    """Retorna a soma de todos os inteiros de n até 1."""
    if n == 1:   # caso base
        return 1
    return n + soma_regressiva(n - 1)


# ---- FUNÇÃO PRINCIPAL ----
def processar_pessoa():
    """Coleta dados, calcula IMC e exibe resultado completo."""

    nome = input("Nome: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    imc = calcular_imc(peso, altura)
    classificacao, emoji = classificar_imc(imc)

    print("\n--- Resultado ---")
    print(f"Nome          : {nome}")
    print(f"IMC           : {imc:.2f} kg/m²")
    print(f"Classificação : {classificacao} {emoji}")


# ---- EXECUÇÃO PRINCIPAL ----
if __name__ == "__main__":

    exibir_cabecalho()

    continuar = "s"

    while continuar == "s":
        processar_pessoa()
        continuar = input("\nProcessar outra pessoa? (s/n): ").lower()

    exibir_rodape()