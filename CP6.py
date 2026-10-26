# CP6 - Comparador de Clubes Brasileiros
# Integrante:
# Eduardo Guzeli - RM 571143

import requests

URL = "https://www.dadosesportivos.com.br/api/campeonato/brasileirao-serie-a/tabela"
tabela = []


def obter_tabela():
    """Consulta a API e retorna os clubes do campeonato."""
    try:
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        if isinstance(dados, dict):
            clubes = dados.get("data", [])
            if isinstance(clubes, list):
                return clubes

        if isinstance(dados, list):
            return dados

        print("A API retornou um formato de dados inesperado.")
        return []

    except requests.exceptions.RequestException:
        print("Erro ao conectar com a API. Verifique sua internet e tente novamente.")
        return []

    except ValueError:
        print("Erro ao interpretar os dados recebidos da API.")
        return []


def nome_clube(clube):
    return clube.get("team", "Desconhecido")


def pontos(clube):
    return clube.get("points", 0)


def vitorias(clube):
    return clube.get("wins", 0)


def saldo_gols(clube):
    return clube.get("gd", 0)


def exibir_tabela():
    """Exibe a classificação do campeonato."""
    if not tabela:
        print("Tabela indisponível.")
        return

    print("\n===== TABELA DO BRASILEIRÃO =====")
    print(f"{'Pos.':<6}{'Clube':<25}{'Pontos':<8}{'Jogos':<8}")
    print("-" * 47)

    for clube in tabela:
        posicao = clube.get("position", "-")
        jogos = clube.get("played", 0)

        print(
            f"{posicao:<6}{nome_clube(clube):<25}"
            f"{pontos(clube):<8}{jogos:<8}"
        )


def buscar_clube(nome):
    """Busca um clube pelo nome."""
    nome = nome.strip().casefold()

    for clube in tabela:
        if nome_clube(clube).casefold() == nome:
            return clube

    return None


def consultar_clube():
    nome = input("Digite o nome do clube: ")
    clube = buscar_clube(nome)

    if clube is None:
        print("Clube não encontrado. Confira a escrita e tente novamente.")
        return

    print("\n===== INFORMAÇÕES DO CLUBE =====")
    print("Nome:", nome_clube(clube))
    print("Posição:", clube.get("position", "N/A"))
    print("Pontos:", pontos(clube))
    print("Jogos:", clube.get("played", 0))
    print("Vitórias:", vitorias(clube))
    print("Empates:", clube.get("draws", 0))
    print("Derrotas:", clube.get("losses", 0))
    print("Gols marcados:", clube.get("goals_for", 0))
    print("Gols sofridos:", clube.get("goals_against", 0))
    print("Saldo de gols:", saldo_gols(clube))


def comparar_clubes(clube1, clube2):
    """Compara clubes por pontos, vitórias e saldo de gols."""
    if clube1 is None or clube2 is None:
        print("Não foi possível comparar os clubes.")
        return

    print("\n===== COMPARAÇÃO DE CLUBES =====")

    for clube in (clube1, clube2):
        print(f"\n{nome_clube(clube)}")
        print("Pontos:", pontos(clube))
        print("Vitórias:", vitorias(clube))
        print("Saldo de gols:", saldo_gols(clube))

    desempenho1 = (
        pontos(clube1),
        vitorias(clube1),
        saldo_gols(clube1)
    )

    desempenho2 = (
        pontos(clube2),
        vitorias(clube2),
        saldo_gols(clube2)
    )

    if desempenho1 > desempenho2:
        print("\nMelhor desempenho:", nome_clube(clube1))
    elif desempenho2 > desempenho1:
        print("\nMelhor desempenho:", nome_clube(clube2))
    else:
        print("\nOs clubes estão empatados nos critérios avaliados.")


def solicitar_comparacao():
    nome1 = input("Digite o nome do primeiro clube: ")
    nome2 = input("Digite o nome do segundo clube: ")

    clube1 = buscar_clube(nome1)
    clube2 = buscar_clube(nome2)

    if clube1 is None:
        print(f"Clube não encontrado: {nome1}")
        return

    if clube2 is None:
        print(f"Clube não encontrado: {nome2}")
        return

    comparar_clubes(clube1, clube2)


def estatisticas_campeonato():
    """Apresenta estatísticas calculadas com os dados da API."""
    if not tabela:
        print("Estatísticas indisponíveis.")
        return

    lider = max(tabela, key=pontos)

    melhor_ataque = max(
        tabela,
        key=lambda clube: clube.get("goals_for", 0)
    )

    melhor_defesa = min(
        tabela,
        key=lambda clube: clube.get("goals_against", 0)
    )

    media_pontos = sum(pontos(clube) for clube in tabela) / len(tabela)

    print("\n===== ESTATÍSTICAS DO CAMPEONATO =====")
    print("Quantidade de clubes:", len(tabela))
    print("Líder em pontos:", nome_clube(lider), "-", pontos(lider), "pontos")
    print(
        "Melhor ataque:",
        nome_clube(melhor_ataque),
        "-",
        melhor_ataque.get("goals_for", 0),
        "gols"
    )
    print(
        "Melhor defesa:",
        nome_clube(melhor_defesa),
        "-",
        melhor_defesa.get("goals_against", 0),
        "gols sofridos"
    )
    print(f"Média de pontos por clube: {media_pontos:.2f}")


def menu():
    global tabela
    tabela = obter_tabela()

    if not tabela:
        print("Não foi possível carregar a tabela. O programa será encerrado.")
        return

    while True:
        print("\n===== COMPARADOR DE CLUBES BRASILEIROS =====")
        print("1 - Exibir tabela do campeonato")
        print("2 - Consultar clube")
        print("3 - Comparar dois clubes")
        print("4 - Estatísticas do campeonato")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_tabela()

        elif opcao == "2":
            consultar_clube()

        elif opcao == "3":
            solicitar_comparacao()

        elif opcao == "4":
            estatisticas_campeonato()

        elif opcao == "5":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Digite um número de 1 a 5.")


if __name__ == "__main__":
    menu()
