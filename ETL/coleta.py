import requests
from datetime import datetime, timedelta
import os



api_key = os.getenv("OPENWEATHER_API_KEY")

print(api_key)
def pegar_dados_api(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            'cidade': dados["name"],
            'temperatura': dados["main"]["temp"],
            'sensacao_termica': dados["main"]["feels_like"],
            'umidade': dados["main"]["humidity"],
            'pressao': dados["main"]["pressure"],
            'clima': dados["weather"][0]["main"],
            'descricao': dados["weather"][0]["description"],
            'vento': dados["wind"]["speed"],
            'data_hora': datetime.fromtimestamp(dados["dt"]).strftime('%d/%m/%Y %H:%M:%S'),
            'latitude': dados["coord"]["lat"],
            'longitude': dados["coord"]["lon"]
        }
    else:
        print(f"⚠️ Erro {resposta.status_code} ao buscar dados.")
        return None
    

def mostrar_previsao_futura(cidade, dias, media_diaria=True):
    hoje = datetime.now()
    data_alvo = (hoje + timedelta(days=dias)).date()

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print(f"⚠️ Erro ao obter dados: {resposta.status_code}")
        return

    dados = resposta.json()

    if media_diaria:
        temperaturas, umidades, descricoes = [], [], []

        for previsao in dados["list"]:
            data_previsao = datetime.fromtimestamp(previsao["dt"]).date()
            if data_previsao == data_alvo:
                temperaturas.append(previsao["main"]["temp"])
                umidades.append(previsao["main"]["humidity"])
                descricoes.append(previsao["weather"][0]["description"])

        if temperaturas:
            temp_media = sum(temperaturas) / len(temperaturas)
            umidade_media = sum(umidades) / len(umidades)
            descricao_mais_comum = max(set(descricoes), key=descricoes.count)
            return{
                'cidade': cidade,
                'temperatura_media': temp_media,
                'umidade_media': umidade_media,
                'descricao_mais_comum': descricao_mais_comum,                          
            }
            
        else:
            print("⚠️ Nenhuma previsão encontrada para esse dia.")
    else:
        print(f"\n📍 Previsão detalhada para {cidade} em {data_alvo.strftime('%d/%m')}:")
        for previsao in dados["list"]:
            data_previsao = datetime.fromtimestamp(previsao["dt"])
            if data_previsao.date() == data_alvo:
                print(f"🕒 {data_previsao.strftime('%Hh')}")
                print(f"🌡️ Temp.: {previsao['main']['temp']}°C")
                print(f"💬 Clima: {previsao['weather'][0]['description']}")
                print("-" * 30)