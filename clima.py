import requests

#Variáveis
API_key = "COLOQUE_SUA_CHAVE_DA_API_AQUI" 
city_name = "DIGITE_O_NOME_DE_UMA_CIDADE"

#URL com nome da cidade, chave da API, unidade de medida e idioma
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=pt_br"

#Requisição
response = requests.get(url)

#Verificação de resultado 
#200 (OK)
#404 (Not Found)
#401 (Unauthorized)
#500 (Internal Server Error)

if response.status_code == 200:
    data = response.json() #Transformação da resposta em um dicionário Python
    
    #Obtenção de dados específicos de dentro do JSON
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
 
    
    #Exibição de informações
    print(f"--- CLIMA ATUAL EM {city_name.upper()} ---")
    print(f"Temperatura: {temp}°C")
    print(f"Condição: {description.capitalize()}")
    print("\n--- Créditos ---")
    print("Dados meteorológicos fornecidos por OpenWeather.")
    print("Licença: Open Data Commons Open Database License (ODbL).")

else:
    #Em caso de erro
    print("Erro ao buscar os dados da API.")
    print(f"Código do erro: {response.status_code}")

