import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY não encontrada! Verifique o arquivo .env")

cidade = "Araci"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric"


response = requests.get(url)

if response.status_code==200:
    dados_clima = response.json()
    print(dados_clima)
else:
    print(f"Erro na requisição: {response.status_code}")