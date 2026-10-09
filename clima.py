import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Obtém a chave da API
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Validação imediata da chave de API
if not API_KEY or API_KEY.strip() == "" or API_KEY == "sua_chave_aqui":
    print("Erro: Chave de API (OPENWEATHER_API_KEY) não configurada.")
    print("Crie um arquivo '.env' na raiz do projeto contendo: OPENWEATHER_API_KEY=sua_chave_aqui")
    exit(1)

LATITUDE = "-3.7319"  # Fortaleza
LONGITUDE = "-38.5267"

# URL da API do OpenWeather
URL = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "units": "metric",
    "lang": "pt_br"
}

try:
    # Requisição com timeout de 10 segundos
    resposta = requests.get(URL, params=params, timeout=10)

    # Tratamento específico de códigos HTTP
    if resposta.status_code == 401:
        print("Erro 401: Chave de API (API Key) inválida ou não autorizada.")
        print("O que fazer:")
        print(" 1. Abra o arquivo '.env' e verifique se a chave foi digitada corretamente sem aspas ou espaços.")
        print(" 2. Se a chave foi criada recentemente no OpenWeather, aguarde a ativação.")
    elif resposta.status_code == 404:
        print("Erro 404: Localização ou recurso não encontrado.")
    elif resposta.status_code != 200:
        print(f"Erro HTTP {resposta.status_code}: {resposta.reason}")
    else:
        dados = resposta.json()
        temperatura = dados["main"]["temp"]
        # Corrigido: acessa o primeiro elemento da lista "weather"
        descricao = dados["weather"][0]["description"].capitalize()
        cidade = dados.get("name", "Fortaleza")

        print("--- CLIMA ATUAL ---")
        print(f"Local: {cidade}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Condição: {descricao}")
        print("-------------------")
        print("Créditos: Dados fornecidos por OpenWeather (ODbL).")

except requests.exceptions.ConnectionError:
    print("Erro de conexão: Não foi possível conectar à internet.")
    print("Verifique sua conexão com a rede e tente novamente.")
except requests.exceptions.Timeout:
    print("Erro de timeout: A requisição demorou mais de 10 segundos para responder.")
    print("O serviço da OpenWeather pode estar instável ou sua rede está lenta.")
except requests.exceptions.RequestException as e:
    print(f"Erro inesperado na requisição: {e}")