import requests
# import json
import pandas as pd

url_negativacoes = "https://api.asaas.com/v3/paymentDunnings"

token_ebramev = "#"

headers = {
    "accept": "application/json",
    "access_token": token_ebramev
}

negativacoes_data = []

pag = 0
limit = 100
while True :

    url_pag = f"{url_negativacoes}?offset={pag}&limit={limit}"
    temp_req = requests.get(url_pag, headers=headers)
    temp_data = temp_req.json()

    if temp_data['hasMore'] == False:
        break

    negativacoes_data.extend(temp_data['data'])
    print(f"Rodou {pag}")
    pag+= limit

df_negativacoes = pd.DataFrame(negativacoes_data)

# Exibindo os dados no Power BI
df_negativacoes

# json_indent = json.dumps(negativacoes_data, indent=2)
# with open("negativacoes.json", "w") as outfile:
#     outfile.write(json_indent)
