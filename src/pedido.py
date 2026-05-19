def calcular_total_pedido(itens, valor_minimo):
    """
    Calcula o valor total do pedido e valida o valor mínimo.

    Parâmetros:
    itens (list): Lista de itens contendo o preço.
    valor_minimo (float): Valor mínimo exigido pelo restaurante.

    Retorna:
    float: Total do pedido.

    Exceções:
    ValueError: Caso o valor mínimo não seja atingido.
    """

    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total