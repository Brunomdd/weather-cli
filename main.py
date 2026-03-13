from utils import linha, cabecalho, leiaint, historico, emoji
from datetime import datetime
from api import api_cidade, api_clima
from storage import carregar, salvar


def main():
    """
    Função principal do programa WEATHER-CLI que gerencia o menu interativo
    para o usuário consultar o clima de cidades, visualizar o histórico de consultas
    e sair da aplicação.

    Fluxo:
    1. Carrega o histórico salvo em arquivo JSON.
    2. Exibe um menu com opções para:
        - Ver histórico de consultas.
        - Fazer uma nova consulta de clima por cidade.
        - Sair do programa.
    3. Se o usuário escolhe nova consulta:
        - Solicita o nome da cidade.
        - Busca os dados da cidade na API BrasilAPI.
        - Se encontrar a cidade, consulta a previsão do tempo.
        - Exibe a previsão formatada com emojis e adiciona ao histórico.
        - Salva o histórico atualizado em arquivo JSON.
    4. Repete o menu até o usuário escolher sair.

    :return: None
    """
    lista = carregar()  # Carrega histórico de consultas do arquivo JSON
    cabecalho("WEATHER-CLI")  # Exibe cabeçalho do programa

    while True:
        print("1 - ver histórico")
        print('2 - nova consulta ')
        print('3 - sair')
        opc = leiaint('escolha uma opção: ')

        if opc == 1:
            historico(lista)  # Exibe o histórico salvo

        elif opc == 2:
            hora_atual = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
            achou = None
            cidade = str(input('cidade: '))

            resposta = api_cidade(cidade)  # Busca dados da cidade na API

            # Procura correspondência exata no nome da cidade
            for c in resposta:
                if c['nome'].strip().lower() == cidade.strip().lower():
                    achou = c
                    break

            if not achou:
                print("não encontramos essa cidade! ")

            if achou:
                print(f"Cidade encontrada: {achou['nome']} - {achou['estado']}")
                clima_tempo = api_clima(achou["id"])  # Busca previsão do tempo

                # Exibe a previsão para os próximos dias
                for clima in clima_tempo['clima']:
                    print(linha())
                    print(f"nome: {achou['nome']}".center(35))
                    print(f"data: {clima['data'][5:10]}".center(35))
                    print(f"condição: {clima['condicao_desc']} {emoji(condicao=clima['condicao_desc'])} ".center(35))
                    print(f"mínima: {clima['min']}".center(35))
                    print(f"maxíma {clima['max']}".center(35))
                    print(linha())

                # Adiciona consulta ao histórico e salva
                lista.append({
                    "nome": achou['nome'],
                    "data": hora_atual,
                    "condição": clima['condicao_desc'],
                    "mínima": clima['min'],
                    "máxima": clima['max']
                })
                salvar(lista)

        elif opc == 3:
            cabecalho('Saindo . . . até mais!')
            break


if __name__ == "__main__":
    main()