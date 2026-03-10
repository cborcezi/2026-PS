# =================================================
# SISTEMA DE PROCESSAMENTO DE NOTAS
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções, Parâmetros, Retorno e Escopo
# Autor      : Cauã Borcezi Ferreira
# Data       : 10/03/2026
# Repositório: https://github.com/cborcezi/2026-PS
# =================================================
#
# DESCRIÇÃO:
# Programa que calcula a média de alunos e determina
# sua situação acadêmica conforme os critérios do IFPR.
# Também apresenta um resumo final da turma.
# =================================================

# ---------- FUNÇÕES BÁSICAS ----------
def calcular_media(nota1, nota2):
    """Recebe duas notas e retorna a média."""
    return (nota1 + nota2) / 2

def verificar_situacao(media):
    """Determina a situação do aluno."""
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

# ---------- FUNÇÕES INTERMEDIÁRIAS ----------
def solicitar_notas(nome_aluno):
    """Solicita e valida notas entre 0 e 10."""

    while True:
        nota1 = float(input(f"Primeira nota de {nome_aluno}: "))
        if 0 <= nota1 <= 10:
            break
        print("Nota inválida. Digite entre 0 e 10.")
    while True:
        nota2 = float(input(f"Segunda nota de {nome_aluno}: "))
        if 0 <= nota2 <= 10:
            break
        print("Nota inválida. Digite entre 0 e 10.")
    return nota1, nota2

def gerar_relatorio(nome, media, situacao):
    """Mostra o resultado do aluno."""
    print("\n--- Resultado ---")
    print(f"Aluno    : {nome}")
    print(f"Média    : {media:.2f}")
    print(f"Situação : {situacao}")

# ---------- FUNÇÕES AVANÇADAS ----------
def calcular_media_turma(medias):
    """Soma as médias usando recursão."""
    # caso base
    if len(medias) == 1:
        return medias[0]
    return medias[0] + calcular_media_turma(medias[1:])

def resumo_turma(alunos):
    """Conta quantos alunos estão em cada situação."""
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    for aluno in alunos:
        if aluno["situacao"] == "Aprovado":
            aprovados += 1
        elif aluno["situacao"] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1
    return aprovados, recuperacao, reprovados

# ---------- PROGRAMA PRINCIPAL ----------
alunos = []
medias = []
print("\n=== PROCESSAMENTO DE NOTAS ===\n")
for i in range(3):

    nome = input(f"\nNome do aluno {i+1}: ")

    nota1, nota2 = solicitar_notas(nome)

    media = calcular_media(nota1, nota2)

    situacao = verificar_situacao(media)

    gerar_relatorio(nome, media, situacao)

    alunos.append({
        "nome": nome,
        "media": media,
        "situacao": situacao
    })
    medias.append(media)

# ---------- RESUMO FINAL DA TURMA ----------
media_turma = calcular_media_turma(medias) / len(medias)
aprovados, recuperacao, reprovados = resumo_turma(alunos)
print("\n====== RESUMO DA TURMA ======")
print(f"Média geral da turma: {media_turma:.2f}")
print(f"Aprovados   : {aprovados}")
print(f"Recuperação : {recuperacao}")
print(f"Reprovados  : {reprovados}")
print("=============================")