def linha(l=42):
    """
    Gera uma linha de separação composta por traços.

    :param l: Comprimento da linha (padrão: 42)
    :type l: int
    :return: String de traços com tamanho especificado
    :rtype: str
    :example: linha(10) -> "----------"
    """
    return "-" * l


def cabecalho(txt):
    """
    Exibe um cabeçalho centralizado com linhas acima e abaixo do texto.

    :param txt: Texto a ser exibido no cabeçalho
    :type txt: str
    :return: None
    :rtype: None
    :example: cabecalho("MENU") imprime:
        ------------------------------------------
                         MENU
        ------------------------------------------
    """
    print(linha())
    print(f"{txt}".center(42))
    print(linha())


def emoji(condicao):
    """
    Retorna um emoji correspondente à condição do tempo.

    :param condicao: Condição do clima (ex: 'Chuva', 'Parcialmente Nublado', 'Ensolarado')
    :type condicao: str
    :return: Emoji representando a condição
    :rtype: str
    :example: emoji('Chuva') -> "🌧️"
    """
    if condicao == 'Chuva':
        return "🌧️"
    elif condicao == "Parcialmente Nublado":
        return "☁️"
    elif condicao == "Ensolarado":
        return "☀️"
    return ""


def leiaint(valor):
    """
    Lê um número inteiro do usuário, repetindo até que a entrada seja válida.

    :param valor: Mensagem de prompt exibida ao usuário
    :type valor: str
    :return: Número inteiro digitado pelo usuário
    :rtype: int
    :example:
        leiaint("Digite um número: ") -> 5
    """
    while True:
        try:
            msg = int(input(valor))
            return msg
        except ValueError:
            print('Erro, digite um número inteiro!')


def historico(lista):
    """
    Exibe o histórico de consultas de clima.

    :param lista: Lista de dicionários contendo o histórico de consultas
                  Cada dicionário deve ter as chaves:
                  'nome', 'data', 'condição', 'mínima', 'máxima'
    :type lista: list
    :return: None
    :rtype: None
    :example:
        historico([{"nome":"São Paulo","data":"13/03/2026","condição":"Chuva","mínima":20,"máxima":28}])
        -> imprime:
            nome: São Paulo - data:13/03/2026 - condição: Chuva - mínima:20 - máxima:28
    """
    if not lista:
        print("O histórico está vazio!")
        return
    for h in lista:
        print(f"nome: {h['nome']} - data:{h['data']} - condição: {h['condição']} - mínima:{h['mínima']} - máxima:{h['máxima']}")