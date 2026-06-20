import requests
def fazer_requisicao(url):
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        return resposta.json()

    except requests.exceptions.ConnectionError:
        print("A API não conseguiu se conectar!")
    except requests.exceptions.Timeout:
        print("O servidor demorou a responder!")
    except requests.exceptions.InvalidURL:
        print("URL inválida")
    except requests.exceptions.RequestException as err:
        print(f"Erro na requisição: {err}")
    except ValueError:
        print("Erro ao interpretar o formato de dados!")
    return None

def api_cidade(nome_cidade):
    url = f"https://brasilapi.com.br/api/cptec/v1/cidade/{nome_cidade}"
    dados = fazer_requisicao(url)
    return dados if dados is not None else []

def api_clima(weather_api):
    url = f"https://brasilapi.com.br/api/cptec/v1/clima/previsao/{weather_api}"
    dados = fazer_requisicao(url)
    return dados if dados is not None else {}