omnitrix = 'HeatBlast'
print(omnitrix)

#Esta condição verifica se o texto "HeatBlast" exixste na variavel "omnitrix", retornando um valor (boolean)booleano.
z = 'HeatBlast' in omnitrix
print(z)

#A função .upper() deixa toda a string com caracteres maiúsculas.
print(omnitrix.upper())

#A função .lower() deixa toda a string com caracteres minúsculas.
print(omnitrix.lower())

#A função .capitalize() deixa o começo de toda caractere string maiuscúcula. 
print(omnitrix.capitalize())

#A função .istrip() remove todos os espaços em branco da sua str  ing, tanto no começo como no final.
print(omnitrix.strip())

#A função .replace() substitui qual texto de sua string por qualquer outro texto.
print(omnitrix.replace('HeatBlast', 'GhostFreak'))

#A função len() diz quantos caracteres tem a sua string.
print(len(omnitrix))

#A função .index() procura o caractere citado e retorna seu índce.
print(omnitrix.index('s'))

#A função .isupper() verifica se todos os caracteres da string são maiúsculas, retornando um valor (boolean)booleano.
print(omnitrix.isupper())

#A função .islower() verifica se todos os caracteres da string são minúsculas, retornando um valor (boolean)booleano.
print(omnitrix.islower())