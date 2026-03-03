# Arquivo: 01b-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

nome = input("Digite o nome do aluno: ")  # ERRO 1: estava "imput", o correto é "input"
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2  # ERRO 2: faltavam parênteses, estava calculando nota1 + (nota2/2)

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")  # ERRO 3: estava "pront", o correto é "print"
# ERRO 4: a média estava sendo calculada incorretamente por causa da precedência de operadores (corrigido na linha da média)