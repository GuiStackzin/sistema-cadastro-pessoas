def classificacao_por_idade(idade):
    """Função para classificar uma pessoa baseado na idade"""
    if idade < 18:
        return "Menor de idade"
    elif idade >= 65:
        return "Aposentável"
    else:
        return "Em idade ativa"