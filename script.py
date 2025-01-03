import requests

def consultar_resultados_loteria(tipo_loteria, numero_concurso):
    """Consulta os resultados de um concurso específico de uma loteria."""
    url_base = "https://servicebus2.caixa.gov.br/portaldeloterias/api/"
    url = f"{url_base}{tipo_loteria}/{numero_concurso}"
    
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            dados = resposta.json()
            numeros = dados.get("listaDezenas", [])
            return numeros, dados.get("dataApuracao", "Data indisponível")
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar os dados: {e}")
        return None, None

def exibir_menu():
    """Exibe o menu principal."""
    print("\n=== Consulta de Resultados de Loterias ===")
    print("1. Mega-Sena")
    print("2. Quina")
    print("3. Lotofácil")
    print("4. Dia de Sorte")
    print("5. Loteca")
    print("6. Dupla Sena")
    print("7. Lotomania")
    print("8. +Milionária")
    print("9. Super Sete")
    print("10. Timemania")
    print("0. Sair")

def main():
    """Função principal do programa."""
    loterias = {
        "1": "megasena",
        "2": "quina",
        "3": "lotofacil",
        "4": "diadesorte",
        "5": "loteca",
        "6": "duplasena",
        "7": "lotomania",
        "8": "maismlvr",
        "9": "supersete",
        "10": "timemania"
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '0':
            print("Encerrando o programa. Até mais!")
            break

        tipo_loteria = loterias.get(opcao)
        if tipo_loteria is None:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            numero_concurso = int(input("Digite o número do concurso: "))
            numeros, data = consultar_resultados_loteria(tipo_loteria, numero_concurso)
            if numeros:
                print(f"\nConcurso {numero_concurso} - {tipo_loteria.capitalize()}")
                print(f"Data: {data}")
                print(f"Números sorteados: {', '.join(numeros)}")
            else:
                print(f"concurso ainda não realizado {numero_concurso}.")
        except ValueError:
            print("Por favor, insira um número de concurso válido!")

if __name__ == "__main__":
    main()
