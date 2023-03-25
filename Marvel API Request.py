import requests
import hashlib
import time
import pandas as pd
import os

def get_Marvel(API_key: str, offset: int = 0, limit: int = 100) -> requests.models.Response:
    
    '''
    Essa função retorna a o corpo da resposta da API dos personagens da Marvel.
    
    ----------
    Parâmetros
    ----------

    API_key : <str>
        Chave pública da API.
    offset : <int>
        Posição de onde a API deve retornar suas respostas.
    limit : <int>
        Quantos itens a API deve retornar. Limitado a 100 por chamada.
        
    -------
    Retorna
    -------
    r : <requests.models.Response>
        Corpo da resposta da chamada de API.
    '''


    timestamp = str(int(time.time()))
    str2hash = timestamp + private_key + public_key
    hash = hashlib.md5(str2hash.encode())
    md5_hash = hash.hexdigest()
    url = f"https://gateway.marvel.com/v1/public/characters?limit={limit}&offset={offset}&ts={timestamp}&apikey={public_key}&hash={md5_hash}"

    return requests.get(url)


def json2df(json: dict) -> pd.core.frame.DataFrame:
    
    '''
    Função que realiza o pré-processamento do corpo da resposta da API da Marvel
    e retorna uma DataFrame pronta do pandas.
    
    ----------
    Parâmetros
    ----------

    json : <dict>
        Dados da resposta da chamada de API da Marvel.
       
    -------
    Retorna
    -------
    
    df : <pandas.core.frame.DataFrame>
        Dataframe pré-processado dos personagens da Marvel.
    '''    

    df0 = {}
    # Buscando os dados que estão disponíveis na raiz
    for i in ['id', 'name', 'description']:
        df0[i] = [hero[i] for hero in json['data']['results']]

    # Buscando os dados que estão disponíveis dentro do branch 'available'
    for i in ['comics', 'series', 'stories', 'events']:
        df0[i] = [hero[i]['available'] for hero in json['data']['results']]

    return pd.DataFrame(df0)


if __name__ == "__main__":
    ## INICIALIZAÇÃO
    public_key = "YOUR_PUBLIC_KEY"
    private_key = "YOUR_PRIVATE_KEY"
    limit = 100

    # Primeiro 'loop'
    r = get_Marvel(public_key, limit = limit)
    json = r.json()
    N_herois =  json['data']['total']
    print('Número de heróis encontrados:', N_herois)
    print('\nBaixando dados...')

    df = json2df(json) # inicialização do DataFrame principal

    ## LOOP PRINCIPAL
    for i in range(limit, N_herois, limit):
        print(f"{(100*len(df)/N_herois):.2f}%")
        r = get_Marvel(public_key, offset = i, limit = limit)
        json = r.json()
        df_temp = json2df(json)
        df = pd.concat([df, df_temp], ignore_index=True)

    ## FINALIZAÇÃO
    print(f"{(100*len(df)/N_herois):.1f}%")
    print("\nDados baixados com sucesso!")
    my_path = os.path.abspath(os.path.dirname(__file__))
    df.to_csv(f'{my_path}\herois.csv', index=False, sep = '|')
    print("Arquivo 'herois.csv' gerado com sucesso!\n")
    #display(df)
    print(df)