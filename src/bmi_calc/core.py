def bmi(peso_kg: float, altura_m: float) -> float:
    """
    Calcula o IMC: peso(kg) / (altura(m) ** 2)
    """
    if peso_kg <= 0:
        raise ValueError("Peso deve ser maior que zero.")
    if altura_m <= 0:
        raise ValueError("Altura deve ser maior que zero.")
    return peso_kg / (altura_m**2)


def category(valor_imc: float) -> str:
    """
    Classifica o IMC segundo faixas padrão da OMS.
    """
    if valor_imc < 18.5:
        return "Abaixo do peso"
    if 18.5 <= valor_imc < 25:
        return "Peso normal"
    if 25 <= valor_imc < 30:
        return "Sobrepeso"
    return "Obesidade"
