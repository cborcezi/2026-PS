# debug_teste/01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!
# Rode de dentro de 05_modulos/: python debug_teste/01b-debug.py


# import Temperatura
# ERRO 1: módulo não existe com esse nome. O correto está em conversores/temperatura.py


from conversores.temperatura import celsius_para_kelvin
from conversores.distancia import km_para_milhas
# ERRO 2: funções estavam sendo importadas do módulo errado


resultado = celsius_para_kelvin(25)
print(f"25°C em K: {resultado}")


from utils.formatador import formatar_resultado

print(formatar_resultado("teste", 100, "km", 62.1, "mi"))
# ERRO 3: havia um argumento extra ("extra") que a função não espera


print(f"50 km = {km_para_milhas(50):.2f} mi")


# from debug_teste import algo
# ERRO 4: tentativa de importar algo que não existe no pacote debug_teste