from utils import linha, cabecalho, leiaint, historico, emoji
from datetime import datetime
from api import api_cidade, api_clima
from storage import carregar, salvar


def consultar():
    nome_cidade = input('cidade: ')
    resposta = api_cidade(nome_cidade)

    for cidade in resposta:
        if cidade['nome'].strip().lower() == nome_cidade.strip().lower():
            return cidade

    return None

def exibir_previsao():
    lista = carregar()
    cidade = consultar()

    if cidade is None:
        print("não encontramos essa cidade!")
        return
    print(f"Cidade encontrada: {cidade['nome']} - {cidade['estado']}")

    clima_tempo = api_clima(cidade["id"])

    for clima in clima_tempo['clima']:
        print(linha())
        print(f"nome: {cidade['nome']}".center(35))
        print(f"data: {clima['data'][5:10]}".center(35))
        print(f"condição: {clima['condicao_desc']} {emoji(condicao=clima['condicao_desc'])}".center(35))
        print(f"mínima: {clima['min']}".center(35))
        print(f"máxima: {clima['max']}".center(35))
        print(linha())

    if clima_tempo['clima']:
        primeiro_dia = clima_tempo['clima'][0]
        hora_atual = datetime.today().strftime("%d/%m/%Y %H:%M:%S")

        lista.append({
            "nome": cidade['nome'],
            "data": hora_atual,
            "condição": primeiro_dia['condicao_desc'],
            "mínima": primeiro_dia['min'],
            "máxima": primeiro_dia['max']
        })
        salvar(lista)


def main():
    lista = carregar()
    cabecalho("WEATHER-CLI")

    while True:
        print("1 - ver histórico")
        print("2 - nova consulta")
        print("3 - sair")
        opc = leiaint("escolha uma opção: ")

        if opc == 1:
            historico(lista)

        elif opc == 2:
            exibir_previsao()
            lista = carregar()

        elif opc == 3:
            cabecalho("Saindo . . . até mais!")
            break

        else:
            print("opção inválida!")


if __name__ == "__main__":
    main()