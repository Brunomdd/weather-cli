import json
from json import JSONDecodeError

def carregar():
    """
    Carrega o histórico de consultas de clima a partir do arquivo JSON.

    Se o arquivo não existir ou estiver vazio/corrompido, retorna uma lista vazia.

    :return: Lista de dicionários contendo o histórico de consultas.
             Cada dicionário deve ter as chaves:
             'nome', 'data', 'condição', 'mínima', 'máxima'.
    :rtype: list
    :example:
        carregar() -> [
            {"nome":"São Paulo","data":"13/03/2026 14:00:00","condição":"Chuva","mínima":20,"máxima":28}
        ]
    """
    lista = []
    try:
        with open("climatempo.json", "r", encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError, JSONDecodeError):
        lista = []
    return lista


def salvar(lista):
    """
    Salva o histórico de consultas de clima em um arquivo JSON.

    Sobrescreve o arquivo existente, formatando o JSON para melhor leitura.

    :param lista: Lista de dicionários contendo o histórico de consultas.
    :type lista: list
    :return: None
    :rtype: None
    :example:
        salvar([{"nome":"São Paulo","data":"13/03/2026 14:00:00","condição":"Chuva","mínima":20,"máxima":28}])
    """
    with open("climatempo.json", "w", encoding="utf-8") as arq:
        json.dump(lista, arq, ensure_ascii=False, indent=2)