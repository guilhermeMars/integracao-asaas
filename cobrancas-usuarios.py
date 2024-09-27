import requests
import json

url_cobranca = "https://api.asaas.com/v3/payments?limit=100"
url_usuarios = "https://api.asaas.com/v3/customers"


token_ebramev = "#"

headers = {
    "accept": "application/json",
    "access_token": token_ebramev
}

response = requests.get(url_cobranca, headers=headers)

cobrancas = response.json()
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

    } for item in cobrancas['data']
]

response = requests.get(url_usuarios, headers=headers)

usuarios = response.json()
usuarios_filtred = [
    {
        "Identificador": item["id"],
        "Nome": item["name"],
        "Email": item["email"],
        "Celular": item["mobilePhone"],
        "Fone": item["phone"],
        "Cpf ou CNPJ": item["cpfCnpj"],
        "Emails adicionais": item["additionalEmails"]
    } for item in usuarios['data']
]

complete_data = {
    "Cobrancas": cobrancas_filtred,
    "Usuarios": usuarios_filtred
}

indent_json = json.dumps(complete_data, indent=2);

# print(json.dumps(cobrancas_filtred, indent=2))
# print("\n")
# print(json.dumps(usuarios_filtred, indent=2))
print(indent_json)
with open("cobrancas_usuarios.json", "w") as outfile:
    outfile.write(indent_json)
