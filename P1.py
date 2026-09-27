LIMITE_DESCONTO = 1000.0
PERCENTUAL_DESCONTO = 0.10

def processar_pedido(dados_pedido: dict [str, int, float]) -> dict [int | float | None]:
    """
        Processa e cadastra um pedido de e-commerce.
    
        Valida os dados do pedido recebido, calcula o valor total
        (aplicando desconto quando aplicável) e retorna um dicionário
        com as informações processadas.
    
        Args:
            dados_pedido (dict): dicionário com os dados do pedido. Deve conter
                as chaves "n" (nome do produto), "p" (preço unitário),
                "q" (quantidade) e "c" (código do produto).
            enviar_email (bool): indica se um e-mail de confirmação deve
                ser enviado ao final do processamento.
    
        Returns:
            dict: dicionário com os dados processados, se tudo for válido.
            bool: False, se nome, preço ou quantidade forem inválidos.
            None: se nenhum dado for informado (dados_pedido is None).
            
        Raises:
        KeyError: se o dicionário 'dados_pedido' não contiver alguma
            das chaves esperadas ("nome", "preco", "quantidade" ou "codigo_produto").
        ValueError: se o valor da chave "c" não puder ser convertido
            para um número inteiro.
            
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

dados_teste = {
    "codigo_pedido": 67,
    "nome": "Notebook alienware 8090",
    "preco": 80000.00,
    "quantidade": 3,
}
def enviar_email():
    pass

try:
    print(processar_pedido(dados_teste))
except ValueError as erro:
    raise ValueError(f"Erro: {erro}")