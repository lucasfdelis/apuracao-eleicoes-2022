# from matplotlib import pyplot as plt
import requests
import time
import pandas as pd

response_API = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
resultado = response_API.json()['cand']

while True:
    hora_atualizacao = response_API.json()['hg']
    candidatos = []
    nvotacoes = []
    pvotacoes = []
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    for data in resultado:
        candidatos.append(data['nm'].replace('&apos;',''))
        nvotacoes.append(data['vap'])
        pvotacoes.append(data['pvap'])
    df = pd.DataFrame({'CANDIDATO':candidatos,'NUMERO DE VOTOS':nvotacoes,'PORCENTAGEM':pvotacoes})
    print(df)
    print("ÚLTIMA ATUALIZAÇÃO:",hora_atualizacao)
    # plt.pie(pvotacoes[0:5],labels=candidatos[0:5])
    # plt.show()
    time.sleep(60)

