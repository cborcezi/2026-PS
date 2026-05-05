'''
==================================================================
# ARQUIVO    : pet.py
# Disciplina : Programação de Sistemas (2026-2)
# Aula       : Aula 20 - Por que POO?
# Autor      : Cauã Borcezi Ferreira
# Conceitos  : Classe, objeto, atributos, métodos, encapsulamento
# Atividade  : Classe Pet
==================================================================
'''

class Pet:
    '''
    Esta classe representa um Pet em um sistema de hotel para pets.
    
    Em vez de guardar os dados do pet em um dicionário solto, como fazíamos na programação estruturada, agora agrupamos os dados e comportamentos dentro de uma classe
    '''

    def __init__(self, nome, especie, idade, raca, peso, porte, dono, vacinado=False, hospedado=False):
        '''
        Método construtor.
        
        Ele é executado automaticamente quando criamos um novo objeto Pet.
        
        Exemplo:
        pet1 = Pet("Rex", "Cachorro", 5, "Labrador", 15.5, "grande", "João")
        
        Parâmetros:
        - nome: nome do pet
        - espécie: espécie do pet
        - idade: idade do pet
        - raca: raça do pet
        - peso: peso do pet
        - porte: porte do pet
        - dono: nome do dono do pet
        - vacinado: se o pet está vacinado (False por padrão)
        '''

        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.hospedado = hospedado
        self.raca = raca
        self.peso = peso
        self.porte = porte
        self.dono = dono
        self.vacinado = vacinado
        

    def exibir_dados(self):
        '''
        Exibe os dados principais do pet.
        '''

        print("\n===== Dados do Pet =====")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso}Kg")
        print(f"Porte: {self.porte}")

    def registrar_entrada(self):
        '''
        Registra a entrada o pet no hotel.
        
        Se o pet ainda não estiver hospedado, muda o atributo hospedado para True.
        '''
        if not self.pode_hospedar():
            return
        
        if self.hospedado:
            print(f"{self.nome} já está hospedado(a).")
        else:
            self.hospedado = True
            print(f"\n{self.nome} entrou no hotel.")

    def pode_hospedar(self):
        if not self.vacinado:
            print(f"\n{self.nome} não pode se hospedar (Vacinação pendente!).")
            return False
        return True

    def registrar_saida(self):
        '''
        Registra a saída do pet do hotel.
        
        Se o pet estiver hospedado, muda o atributo "hospedado" para False.
        '''
        if not self.validar_hospedagem():
            return
        self.hospedado = False
        print(f"\n{self.nome} saiu do hotel.")
    
    def calcular_diaria(self):
        '''
        Calcula o valor da diária do pet.

        - Pet com idade de até 3 anos: R$ 65,00
        - Pet com idade entre 4 e 10 anos: R$ 95,00
        - Pet com mais de 10 anos: R$ 150,00
        '''
        if self.idade <=3:
            diaria = 65.00
        elif 4 <= self.idade <=10:
            diaria = 95.00
        else: 
            diaria = 150.00
        return diaria
    
    def verificar_vacinacao(self):
        '''
        Verifica se o pet está vacinado.

        Se o pet estiver vacinado, exiba:
        - "Vacinação em dia."
        Caso contrário, exiba:
        - "Atenção: vacinação pendente!"
        '''
        if self.vacinado:
            print("\nVacinação em dia.")
        else:
            print("\nAtenção: vacinação pendente!")
        
    def atualizar_peso(self, novo_peso):
        '''
        Atualiza o peso do pet.
        '''
        self.peso = novo_peso
        print(f"O peso de {self.nome} foi atualizado para {self.peso}Kg.")

    def validar_hospedagem(self):
        if self.hospedado:
            print(f"\n{self.nome} já está hospedado(a) no hotel.")
            return True
        else:
            print(f"\n{self.nome} não está hospedado(a) no hotel.")
            return False

    def emitir_resumo(self):
        '''
        Exibir um resumo geral do pet. Deve conter:
        - Nome do pet:
        - Espécie:
        - Idade: 
        - Nome do dono: 
        - Peso:
        - Status de vacinação:
        - Status de hospedagem:
        - Valor da diária:
        '''
        # Status de vacinação
        if self.vacinado:
            status_vacinacao = "Vacinação em dia."
        else:
            status_vacinacao = "Atenção: vacinação pendente!"
        
        # Status de hospedagem
        if self.hospedado:
            status_hospedagem = "Hospedado no hotel."
        else:
            status_hospedagem = "Não está hospedado no hotel."
        
        # Calculando o valor da diária
        valor_diaria = self.calcular_diaria()

        # Emissão do resumo
        resumo = (f"\n----- Resumo do pet -----\n"
                  f"Nome: {self.nome}\n"
                  f"Espécie: {self.especie}\n"
                  f"Idade: {self.idade} anos\n"
                  f"Nome do(a) dono(a): {self.dono}\n"
                  f"Peso: {self.peso}Kg\n"
                  f"Status de Vacinação: {status_vacinacao}\n"
                  f"Status de Hospedagem: {status_hospedagem}\n"
                  f"Valor da Diária: R$ {valor_diaria:.2f}")
        
        print(resumo)


'''
# ==================================================================
# TESTES DA CLASSE
# ==================================================================
# Depois de completar a classe, crie pelo menos 3 objetos Pet.
#
# Exemplo:
# pet1 = Pet("Rex", "Cachorro, 5)
#
# Atenção:
# Se você adicionou novos parâmetros no __init__, será necessário
# informar esses dados na criação do objeto.
# ==================================================================
'''
# Criando os objetos Pet
pets = []
pets = []
pets.append(Pet("Billy", "Cachorro", 4, "Beagle", 11.0, "Médio", "Matheus", True))
pets.append(Pet("Dakota", "Cachorro", 6, "Schnauzer gigante", 40.0, "Grande", "Micheli", True, True))
pets.append(Pet("Estrela", "Gato", 2, "Persa", 5.0, "Pequeno", "Amanda", True))
pets.append(Pet("Hórus", "Cachorro", 5, "Pastor Belga Malinois", 27.5, "Grande", "Bruna", True))
pets.append(Pet("Matias", "Cachorro", 4, "Spitz Alemão", 9.5, "Pequeno", "Alice", True, True))
pets.append(Pet("Paçoca", "Cachorro", 8, "Vira-lata", 16.0, "Médio", "Márcio", False))

for pet in pets:
    pet.exibir_dados()
    pet.registrar_entrada()
    pet.verificar_vacinacao()
    pet.emitir_resumo()