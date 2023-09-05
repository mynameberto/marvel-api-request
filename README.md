# README para o Projeto Marvel Data Collector
## Descrição
Este projeto realiza chamadas à API da Marvel para coletar informações sobre os personagens, processa a resposta em formato JSON e, em seguida, salva os dados coletados em um arquivo CSV.

## Pré-requisitos
- Python 3.x
- Bibliotecas:
    - requests
    - hashlib
    - time
    - pandas
    - os

## Como Usar
1. Obtenha sua chave pública e privada do portal de desenvolvedores da Marvel.
2. Insira sua chave pública e privada nos lugares indicados no código.
3. Execute o script. Ao ser executado, ele fará chamadas sequenciais à API da Marvel para obter detalhes dos personagens.
4. Depois de coletar todas as informações, o script salvará os dados em um arquivo chamado herois.csv.

## Funções Principais
* get_Marvel(): Esta função realiza chamadas à API da Marvel para obter informações sobre os personagens. Ela usa os parâmetros fornecidos, como offset, limit e sua API_key, para personalizar as chamadas.

* json2df(): Depois de obter a resposta da API em formato JSON, esta função é usada para processar os dados e transformá-los em um DataFrame do pandas.

## Fluxo Principal
O fluxo principal do código começa obtendo as informações dos primeiros ***'limit'*** (padrão 100) personagens e depois entra em um loop para coletar os dados restantes em blocos de ***'limit'*** personagens por vez. Uma vez que todos os dados são coletados, eles são concatenados em um único DataFrame e, em seguida, salvos em um arquivo CSV.