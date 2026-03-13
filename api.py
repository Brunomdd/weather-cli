import requests

def api_cidade(city_api):
    """
    Consulta informações de uma cidade na API BrasilAPI (CPTEC).

    Busca cidades correspondentes ao nome informado e retorna os dados em formato JSON.

    :param city_api: Nome ou identificador da cidade a ser consultada.
    :type city_api: str
    :return: Lista de dicionários com informações das cidades encontradas. Retorna
             lista vazia em caso de erro de conexão, timeout, JSON inválido ou URL incorreta.
    :rtype: list
    :example:
        api_cidade("São Paulo") -> [
            {"id": 3550308, "nome": "São Paulo", "estado": "SP"}
        ]
    """
    try:
        city_api = requests.get(f"https://brasilapi.com.br/api/cptec/v1/cidade/{city_api}", timeout=5)
        city_api.raise_for_status()
        return city_api.json()

    except requests.exceptions.ConnectionError:
        print("A API não conseguiu se conectar!")
    except requests.exceptions.Timeout:
        print("O servidor demorou a responder!")
    except requests.exceptions.JSONDecodeError:
        print("Erro ao interpretar o formato de dados!")
    except requests.exceptions.InvalidURL:
        print("URL inválida")
    except requests.exceptions.RequestException as err:
        print(f"Erro na requisição: {err}")
    return []


def api_clima(weather_api):
    """
    Consulta a previsão do tempo para uma cidade usando a API BrasilAPI (CPTEC).

    Recebe o ID da cidade e retorna a previsão do tempo em formato JSON.

    :param weather_api: ID da cidade para a qual se deseja consultar a previsão.
    :type weather_api: int
    :return: Dicionário contendo a previsão do tempo (clima) para os próximos dias.
             Retorna lista vazia em caso de erro de conexão, timeout, JSON inválido ou URL incorreta.
    :rtype: dict
    :example:
        api_clima(3550308) -> {
            "clima": [
                {"data": "2026-03-13", "condicao_desc": "Chuva", "min": 20, "max": 28},
                ...
            ]
        }
    """
    try:
        weather_api = requests.get(f"https://brasilapi.com.br/api/cptec/v1/clima/previsao/{weather_api}", timeout=5)
        weather_api.raise_for_status()
        return weather_api.json()

    except requests.exceptions.ConnectionError:
        print("A API não conseguiu se conectar!")
    except requests.exceptions.Timeout:
        print("O servidor demorou a responder!")
    except requests.exceptions.JSONDecodeError:
        print("Erro ao interpretar o formato de dados!")
    except requests.exceptions.InvalidURL:
        print("URL inválida")
    except requests.exceptions.RequestException as err:
        print(f"Erro na requisição: {err}")
    return []