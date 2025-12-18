import requests

def Conversor(url, nome_html):
    response = requests.get(url)
    nome_html += ".html"
    with open(nome_html, "w", encoding="utf-8") as arquivo:
        arquivo.write(response.text)

while True:

    print("Digite a url do site que deseja converter:")
    url = input("...")
    print("Qual nome eu chamo o arquivo HTML:")
    nome_html = input("...")

    if "" or " " in nome_html:
        print(f"{nome_html} CONTEM ESPAÇOS")
        continue

    if "" or " " in url:
        print(f"{url} CONTEM ESPAÇOS")
        continue

    Conversor(url, nome_html)

    print("ARQUIVO CRIADO COM SUCESSO")

    print("Escolha uma opção:")
    print("1-Criar outro arquivo")
    print("2-SAIR")
    opcao = input("...")

    if opcao == "1":
        continue
    if opcao == "2":
        break
