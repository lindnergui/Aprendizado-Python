import requests


def verifica_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[92mO site {url} está acessível.\033[0m")
        else:
            print(f"\033[91mO site {url} retornou o código {response.status_code}.\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"\033[91mErro ao acessar o site {url}: {e}\033[0m")


url = input("Digite o URL do site: ")
verifica_site(url)
