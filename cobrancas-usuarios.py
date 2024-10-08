import requests
import pandas as pd

# Endpoints utilizados utilizadas
url_cobranca = "https://api.asaas.com/v3/payments"
url_usuarios = "https://api.asaas.com/v3/customers"

# Adicione o token #
token_ebramev = "#"

headers = {
    "accept": "application/json",
    "access_token": token_ebramev
}

cobranca_data = []

pag = 0
limit = 10

# Paginação
while True :

    url_pag = f"{url_cobranca}?offset={pag}&limit={limit}&dateCreated[ge]=2022-06-15"
    temp_req = requests.get(url_pag, headers=headers)
    temp_data = temp_req.json()

    # Campos salvos na requisição
    cobrancas_filtred = [
        {
            "Identificador": item["id"],
            "Data de criacao": item["dateCreated"],
            "Usuario": item["customer"],
            "Valor": item["value"],
            "Valor original": item["originalValue"],
            "Descricao": item["description"],
            "Tipo de cobranca": item["billingType"],
            "Situacao": item["status"],
            "Vencimento": item["dueDate"],
            "Vencimento original": item["originalDueDate"],
            "Data de Pagamento": item["paymentDate"],
            "Data de credito": item["creditDate"],
            "Forma de pagamento": item["billingType"],
            "Data estimada de Credito": item["estimatedCreditDate"],
            **({"Data de confirmacao": item["confirmedDate"]} if "confirmedDate" in item else {}),
            "Valor Liquido": item["netValue"],
            "Numero da fatura": item["invoiceNumber"]

        } for item in temp_data['data']
    ]

    # Finaliza quando acabar as páginas
    if temp_data['hasMore'] == False:
        break

    cobranca_data.extend(cobrancas_filtred)

    pag+= limit

# Lógica duplicada para usuários. Poderia ser feito via função 

usuarios_data = []

pag = 0
limit = 10

while True :

    url_pag = f"{url_usuarios}?offset={pag}&limit={limit}"
    temp_req = requests.get(url_pag, headers=headers)
    temp_data = temp_req.json()

    usuarios_filtred = [
        {
            "Identificador": item["id"],
            "Nome": item["name"],
            "Email": item["email"],
            "Celular": item["mobilePhone"],
            "Fone": item["phone"],
            "Cpf ou CNPJ": item["cpfCnpj"],
            "Emails adicionais": item["additionalEmails"]
        } for item in temp_data['data']
    ]

    if temp_data['hasMore'] == False:
        break

    usuarios_data.extend(usuarios_filtred)

    pag+= limit

df_cobrancas = pd.DataFrame(cobranca_data)
df_usuarios = pd.DataFrame(usuarios_data)

# Exibindo os dados no Power BI
df_cobrancas
df_usuarios

# # Caso quiera salvar os dados em JSON

# json_indent = json.dumps(cobranca_data, indent=2)
# with open("cobrancas.json", "w") as outfile:
#     outfile.write(json_indent)
