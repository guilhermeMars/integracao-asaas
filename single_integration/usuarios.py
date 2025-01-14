import requests
# import json
import pandas as pd

url_usuarios = "https://api.asaas.com/v3/customers"

token_ebramev = "#"

headers = {
    "accept": "application/json",
    "access_token": token_ebramev
}

usuarios_data = []

pag = 0
limit = 100
while True :

    url_pag = f"{url_usuarios}?offset={pag}&limit={limit}"
    temp_req = requests.get(url_pag, headers=headers)
    temp_data = temp_req.json()

    if temp_data['hasMore'] == False:
        break

    usuarios_data.extend(temp_data['data'])
    print(f"Rodou {pag}")
    pag+= limit

df_usuarios = pd.DataFrame(usuarios_data)

# Exibindo os dados no Power BI
df_usuarios

# json_indent = json.dumps(usuarios_data, indent=2)
# with open("usuarios.json", "w") as outfile:
#     outfile.write(json_indent)
