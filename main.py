import pandas as pd
from twilio.rest import Client

# Passo a passo de solução

# Your Account SID from twilio.com/console
#account_sid = "ACab67f8b7d8771a20fcea176c0f3ea1c6"
account_sid = "AC53f3e83952a33a581b55e600e87b6d63"
# Your Auth Token from twilio.com/console
#auth_token  = "4af82ef128e137a9a79aabcc23ab30ac"
auth_token  = "d82f908421df89648d0e4580b10f0ec7"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
listaMeses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in listaMeses:
    #print(mes)
    tabelaVendas = pd.read_excel(f"{mes}.xlsx")

    #print(tabelaVendas)

    linha = tabelaVendas["Vendas"] > 55000
    if (tabelaVendas["Vendas"] > 55000).any():
        vendedor = tabelaVendas.loc[linha,"Vendedor"].values[0]
        vendas = tabelaVendas.loc[linha, "Vendas"].values[0]
        print(f"No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")

        message = client.messages.create(
            #to="+5511962123215",
            to="+5511960438089",
            #from_="+16626707243",
            from_="+17406796789",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
# Para cada arquivo:

# Verificar se algum valor na coluna de vendas daquele arquivo é maior que 55.000

# se for maior do que 55.000 -> Envia um SMS com nome, mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada