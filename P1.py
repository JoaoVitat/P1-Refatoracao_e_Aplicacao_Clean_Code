# Função que processa e cadastra o produto/pedido
def proc_ped(d, env_mail):
 # verifica se o pedido tem dados
 if d == None:
 print("Erro")
 return None

 # pega o nome e preco
 n = d["n"]
 p = d["p"]
 q = d["q"]

 # valida nome
 if n == "":
 print("Nome invalido")
 return False

 # valida preco e quantidade
 if p <= 0 or q <= 0:
 print("Preco ou quantidade invalida")
 return False

 # calcula o total
 t = p * q

 # aplica desconto se for acima de 1000
 if t > 1000:
 # aplica 10% de desconto
 t = t * 0.90

 # converte codigo para inteiro
 c = int(d["c"])

 # exibe se envia email
 if env_mail == True:
 print("Enviando e-mail de confirmacao para o pedido...")

 # cria o dicionario do produto processado
 res = {
 "codigo": c,
 "nome": n,
 "preco_unitario": p,
 "quantidade": q,
 "total_calculado": t
 }

 return res
# Teste do código
try:
 dados_input = {"c": "101", "n": "Teclado Mecânico", "p": 150.0, "q": 8}
 resultado = proc_ped(dados_input, True)
 print("Resultado:", resultado)
except:
 print("Ocorreu algum erro no sistema.")
