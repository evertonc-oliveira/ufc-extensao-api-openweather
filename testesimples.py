import json
import urllib.request

API_KEY = "chavedaapi"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Fortaleza,BR&units=metric&lang=pt_br&appid={API_KEY}"

with urllib.request.urlopen(url) as resposta:
    dados = json.load(resposta)

print(f"Cidade: {dados['name']}")
print(f"Temperatura: {dados['main']['temp']} °C")
print(f"Clima: {dados['weather'][0]['description']}")