# conversores/distancia.py

def km_para_milhas(km):
    """Converte quilômetros para milhas."""
    return km * 0.621371


def milhas_para_km(milhas):
    """Converte milhas para quilômetros."""
    return milhas / 0.621371


def metros_para_pes(metros):
    """Converte metros para pés."""
    return metros * 3.28084


if __name__ == "__main__":
    # Este bloco executa apenas se distancia.py for rodado diretamente

    print("Testando distancia.py...")
    # Teste 1
    print(f"10 km = {km_para_milhas(10):.2f} milhas (esperado ≈ 6.21)")
    # Teste 2
    print(f"5 milhas = {milhas_para_km(5):.2f} km (esperado ≈ 8.05)")
    print("Testes concluídos!")