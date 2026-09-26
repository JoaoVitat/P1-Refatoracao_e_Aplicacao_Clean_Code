LIMITE_DESCONTO = 1000.0
PERCENTUAL_DESCONTO = 0.90


def processar_pedido(dados_pedido: dict | None, enviar_email: bool) -> dict | bool | None:
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
            das chaves esperadas ("n", "p", "q" ou "c").
        ValueError: se o valor da chave "c" não puder ser convertido
            para um número inteiro.
            
    """
    if dados_pedido is None:
        print("Erro")
        return None

    nome = dados_pedido["n"]
    preco = dados_pedido["p"]
    quantidade = dados_pedido["q"]

    if nome == "":
        print("Nome invalido")
        return False

    if preco <= 0 or quantidade <= 0:
        print("Preco ou quantidade invalida")
        return False

    total_calculado = preco * quantidade

    if total_calculado > LIMITE_DESCONTO:
        total_calculado = total_calculado * PERCENTUAL_DESCONTO

    codigo_pedido = int(dados_pedido["c"])

    if enviar_email:
        print("Enviando e-mail de confirmacao para o pedido...")

    pedido_processado = {
        "codigo": codigo_pedido,
        "nome": nome,
        "preco_unitario": preco,
        "quantidade": quantidade,
        "total_calculado": total_calculado
    }

    return pedido_processado

try:
    dados_entrada = {"c": "101", "n": "Teclado Mecânico", "p": 150.0, "q": 8}
    resultado_processamento = processar_pedido(dados_entrada, enviar_email=True)
    print("Resultado:", resultado_processamento)
except (KeyError, ValueError) as erro:
    print("Ocorreu um erro ao processar o pedido:", erro)
