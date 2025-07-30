import csv  # 1. Importa a biblioteca que lê arquivos CSV

# 2. Abre o arquivo 'arquivos.csv' para leitura
with open('site.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)  # 3. Lê o conteúdo como dicionários (um por linha)

    # 4. Para cada linha (ou artigo) do arquivo:
    for linha in leitor:
        autores = linha["Author(s)"]  # 5. Pega a lista de autores da linha
        if "Ramírez" in autores and "Damián" in autores:  # 6. Verifica se o nome está presente
            # 7. Se o nome estiver, mostra as informações abaixo:
            print("-" * 50)  # 8. Imprime linha separadora
            print("Título:", linha["Title"])
            print("Autores:", linha["Author(s)"])
            print("Fonte:", linha["Source"])
            print("Revista:", linha["Journal"])
            print("Idioma(s):", linha["Language(s)"])
            print("Ano de Publicação:", linha["Publication year"])
            print("-" * 50)  # 8. Imprime linha separadora