LIMITE_DESCONTO: float = 1000.0
PERCENTUAL_DESCONTO: float = 0.10

def processar_pedido(dados_pedido: dict[str, str | int | float]) -> dict[str, str | int | float]:
    """
    Processa e cadastra um pedido de e-commerce.

    Valida os dados do pedido recebido, calcula o valor total
    (aplicando desconto quando o total passa do limite) e retorna
    um dicionário com as informações processadas.

    Args:
        dados_pedido (dict[str, str | int | float]): dados do pedido.
            Deve conter as chaves "codigo_pedido", "nome", "preco"
            e "quantidade".

    Returns:
        dict[str, str | int | float]: dicionário com as chaves "codigo",
            "nome", "preco", "quantidade" e "total_calculado".

    Raises:
        ValueError: se faltar alguma chave obrigatória, se algum valor
            não puder ser convertido para o tipo esperado, se o nome
            estiver vazio ou se o preço ou a quantidade forem menores
            ou iguais a zero.
    """
    try:
        codigo_pedido = int(dados_pedido["codigo_pedido"])
        nome = str(dados_pedido["nome"].strip())
        preco = float(dados_pedido["preco"])
        quantidade = int(dados_pedido["quantidade"])

    except (KeyError) as erro:
        raise ValueError(f"Campo obrigatório ausente: {erro}")
    
    except (TypeError, ValueError) as erro:
        raise ValueError(f"erro nos dados do pedido: {erro}")

    if not nome:
        raise ValueError("o nome do produto não pode ser vazio.")

    if preco <= 0 :
        raise ValueError("O preço deve ser maior que zero")

    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")

    total_calculado = preco * quantidade

    if total_calculado > LIMITE_DESCONTO:
        total_calculado *=  (1 - PERCENTUAL_DESCONTO) 

    pedido_processado = {
        "codigo": codigo_pedido,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "total_calculado": total_calculado
    }

    return pedido_processado

dados_teste: dict[str, str | int | float] = {
    "codigo_pedido": 67,
    "nome": "Notebook alienware 8090",
    "preco": 80000.00,
    "quantidade": 3,
}
def enviar_email() -> None:
    pass

try:
    print(processar_pedido(dados_teste))
except ValueError as erro:
    raise ValueError(f"Erro: {erro}")