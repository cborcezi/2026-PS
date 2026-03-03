# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

catalogo = [

    {"titulo": "Código Limpo",
     "autor": "Robert C. Martin",
     "disponivel": True},

    {"titulo": "Entendendo Algoritmos",
     "autor": "Aditya Bhargava",
     "disponivel": False},

    {"titulo": "Python Fluente",
     "autor": "Luciano Ramalho",
     "disponivel": True},
]

# ERRO 1: índice 3 não existe (lista vai de 0 a 2)
print("Primeiro livro:", catalogo[0]["titulo"])

print("\nLivros disponíveis:")

for livro in catalogo:

    # ERRO 2: condição estava verificando == False (lógica invertida)
    if livro["disponivel"]:
        print(f'  {livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros: {total}")

# ERRO 3: faltava .items() para iterar chave e valor corretamente
for chave, valor in catalogo[0].items():
    print(f" {chave}: {valor}")

# ERRO 4: chave estava como "Autor" (maiúsculo), mas no dicionário é "autor"
primeiro_autor = catalogo[0]["autor"]

print("\nAutor do primeiro livro:", primeiro_autor)