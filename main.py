def classificar_idade(idade):
    if not isinstance(idade, int):
        raise TypeError("A idade deve ser um número inteiro.")
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 64:
        return "Adulto"
    else:
        return "Idoso"

