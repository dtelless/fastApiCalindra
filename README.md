# 1️⃣ Projeto Backend Calindra

O projeto consiste na construção de uma API REST que consuma a API de Geolocalização do Google e retorne:

•  Uma API Rest

•  A API receberá três ou mais endereços como parâmetros de entrada

•  O sistema deverá obter a latitude e longitude dos endereços usando um serviço de geocoding
de terceiros (google maps, geoapify, etc..)

•  O sistema deverá calcular a distância entre cada um dos endereços

•  A API deverá responder uma lista com todas as distâncias obtidas entre os endereços e também o 
par de endereços mais próximos e o par de endereços mais distantes.https://myprojects.geoapify.com


## 🛠️ Tecnologias e ferramentas utilizadas

- Python
- FastAPI  (https://pypi.org/project/fastapi/)
- Googlemaps (https://pypi.org/project/googlemaps/)
- Geopy 2.3.0 (https://pypi.org/project/geopy/)

## 🌟 Rodando a aplicação

### Requerimentos

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)
<br>

### Siga as etapas para a aplicação funcionar corretamente:

<br>

#### 🟢 No terminal bash (Git), clone este repositório

```
git clone https://github.com/dtelless/fastApiCalindra.git
```

<br>

#### 🟢 Acesse a pasta do projeto pelo terminal

```
cd fastApiCalindra
```

<br>

#### 🟢 Certificar-se que o pacote pip e Venv de ambbientes virtuais do Python está instalado

No Linux
```
sudo apt install python3-pip
sudo pip install virtualenv
```
No Windows
````
pip install virtualenv

````

<br>

#### 🟢 Ativando Ambiente virtual e instalando pacotes necessários

No Linux
```
python3 -m venv venv
source venv/bin/activate
```

No Windows
```
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

<br>

#### 🟢 Acesse o arquivo `.env` e Altere a chave da API para a sua., caso não tenha criar em https://console.cloud.google.com/apis/credentials: 

```

# APIs
APIKEY='Sua chave aqui'
```

#### 🟢 Rode a API

```
 python main.py
```

#### Você verá essa mensagem: `INFO:     Uvicorn running on http://127.0.0.1:8000`.

<br>

## 🔃 Rotas da API

### 🪧 `/adresses`

Rota para <b>encontrar</b> todas as distâncias de acordo com as localizações informadas.<br>
Método: `POST`<br>

Template para enviar os dados:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/adresses' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
   "adresses":
   [
       {"address": "Av. Rio Branco, 1 Centro, Rio de Janeiro RJ,20090003"},
       {"address": "Praça Mal. Âncora, 122 Centro, Rio de Janeiro RJ, 20021200"},
       {"address": "Rua 19 de Fevereiro, 34 Botafogo, Rio de Janeiro RJ, 22280030"}
   ]
}'
```

Resposta:
````
{
    "status": "SUCCESS",
    "data": {
        "distances": [
            {
                "pinA": "Av. Rio Branco, 1 Centro, Rio de Janeiro RJ,20090003",
                "pinB": "Rua 19 de Fevereiro, 34 Botafogo, Rio de Janeiro RJ, 22280030",
                "distance": 5960
            },
            {
                "pinA": "Praça Mal. Âncora, 122 Centro, Rio de Janeiro RJ, 20021200",
                "pinB": "Rua 19 de Fevereiro, 34 Botafogo, Rio de Janeiro RJ, 22280030",
                "distance": 5476
            },
            {
                "pinA": "Av. Rio Branco, 1 Centro, Rio de Janeiro RJ,20090003",
                "pinB": "Praça Mal. Âncora, 122 Centro, Rio de Janeiro RJ, 20021200",
                "distance": 1253
            }
        ],
        "nearest": [
            {
                "pinA": "Av. Rio Branco, 1 Centro, Rio de Janeiro RJ,20090003",
                "pinB": "Praça Mal. Âncora, 122 Centro, Rio de Janeiro RJ, 20021200",
                "distance": 1253
            }
        ],
        "farest": [
            {
                "pinA": "Av. Rio Branco, 1 Centro, Rio de Janeiro RJ,20090003",
                "pinB": "Rua 19 de Fevereiro, 34 Botafogo, Rio de Janeiro RJ, 22280030",
                "distance": 5960
            }
        ]
    }
}

````

<br>
