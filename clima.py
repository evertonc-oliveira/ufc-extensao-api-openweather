import requests

# Configurações da requisição
API_KEY = "COLOQUE_SUA_CHAVE_DA_API_AQUI"
LATITUDE = "-3.7319"  # Fortaleza
LONGITUDE = "-38.5267"

# Corrigido {LATITUDEy -> {LATITUDE}
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    # Requisição com timeout de 10 segundos
    resposta = requests.get(URL, timeout=10)

    # Tratamento específico de códigos HTTP
    if resposta.status_code == 401:
        print("Erro 401: Chave de API (API Key) inválida ou não autorizada.")
        print("Verifique se sua chave no OpenWeather foi copiada corretamente ou aguarde alguns minutos se foi criada recentemente.")
    elif resposta.status_code == 404:
        print("Erro 404: Localização ou recurso não encontrado.")
    elif resposta.status_code != 200:
        print(f"Erro na requisição (Código {resposta.status_code}): {resposta.reason}")
    else:
        dados = resposta.json()
        
        # Corrigido dados["main"][temp"] -> dados["main"]["temp"]
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"].capitalize()
        cidade = dados.get("name", "Fortaleza")

        # Corrigido a formatação das f-strings e emojis
        print("--- CLIMA ATUAL ---")
        print(f" Local: {cidade}")
        print(f" Temperatura: {temperatura}°C")
        print(f" Condição: {descricao}")
        print("------------------")
        print("Créditos: Dados fornecidos por OpenWeather (ODbL).")

except requests.exceptions.ConnectionError:
    print("Erro de conexão: Não foi possível conectar à internet. Verifique sua rede e tente novamente.")
except requests.exceptions.Timeout:
    print("Erro de timeout: A requisição demorou muito para responder. Tente novamente mais tarde.")
except requests.exceptions.RequestException as e:
    print(f"Erro inesperado na comunicação com a API: {e}")