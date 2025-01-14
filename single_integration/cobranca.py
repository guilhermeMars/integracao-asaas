import requests
import re
# import json
import pandas as pd

url_cobranca = "https://api.asaas.com/v3/payments"

token_ebramev = "#"

headers = {
    "accept": "application/json",
    "access_token": token_ebramev
}

cobranca_data = []

pag = 0
limit = 100

while True :
    url_pag = f"{url_cobranca}?offset={pag}&limit={limit}&dateCreated[ge]=2022-06-15"
    temp_req = requests.get(url_pag, headers=headers)
    temp_data = temp_req.json()

    if temp_data['hasMore'] == False:
        break
    
    for item in temp_data['data']:
        descricao = item["description"]

        all_results = re.findall(r'T\d{1,3}-[A-Z]+(?:\s[A-Z]+)*|[A-Z]+(?:\s[A-Z]+)*(?:\s-\s\d{1,2})?|[A-Z]+(?:\s[A-Z]+)*', descricao)
        for result in all_results:
            if len(result) > 3:
                item["curso"] = result
    
    print(f"Rodou {pag}")
    pag+= limit
    cobranca_data.extend(temp_data['data'])


df_cobrancas = pd.DataFrame(cobranca_data)

# Exibindo os dados no Power BI
df_cobrancas

# json_indent = json.dumps(cobranca_data, indent=2)
# with open("cobrancas-1.json", "w") as outfile:
#     outfile.write(json_indent)
