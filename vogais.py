nome = "exagerado_letra.txt"
vogais = 'aeiou'.lower()

arquivo = open(nome, "r", encoding="utf-8")

conteudo = arquivo.read()

conteudo = conteudo.lower()

conteudo = conteudo.replace('á','a').replace('à','a').replace('ã','a').replace('â','a')
conteudo = conteudo.replace('é','e').replace('ê','e')
conteudo = conteudo.replace('í','i')
conteudo = conteudo.replace('ó','o').replace('õ','o').replace('ô','o')
conteudo = conteudo.replace('ú','u')

contagem = {vogal: 0 for vogal in vogais}

for char in conteudo:
    if char in contagem:
        contagem[char] += 1

print(f"A quantidade de vezes que as vogais {vogais} aparecem é: {contagem}")