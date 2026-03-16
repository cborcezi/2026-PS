def validar_numero(valor_str, minimo=None, maximo=None):
    """
    Tenta converter uma string para número e verifica limites.
    Retorna (True, numero) ou (False, mensagem de erro)
    """

    try:
        numero = float(valor_str)
    except ValueError:
        return False, "Valor inválido."
    if minimo is not None and numero < minimo:
        return False, f"O valor deve ser maior ou igual a {minimo}."
    if maximo is not None and numero > maximo:
        return False, f"O valor deve ser menor ou igual a {maximo}."
    return True, numero