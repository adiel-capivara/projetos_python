faturamento = 1000
custo = 600
lucro = faturamento - custo

#para exibir textos com variáveis existe três tipos de concatenação

#como o + e transformando todas as variáveis em string usando a função str()
texto = "o lucro foi de " + str(lucro) + "e o faturamento foi de " + str(faturamento)
print(texto)

#usando a vírgula, que já transforma as variáveis em string automaticamente
print("o lucro foi de", lucro, "e o faturamento foi de", faturamento)

#ou usando f-strings, e colocando as variáveis entre chaves {}
print(f"o lucro foi de {lucro} e o faturamento foi de {faturamento}")


#formatando textos

#para deixar o texto com todas as letras minusculas, use a função lower()
email = 'EMAIL_FALSO@gmail.com'
print(email.lower()) 

#para eliminar espaços inuteis no começo e no final do texto, use a função strip()
nome = '   Adiel   '
nome = nome.strip()
print(nome)

#para deixar o texto com todas as letras maiusculas, use a função upper()
nome = 'Adiel'
print(nome.upper())

#para saber o tamanho de um texto use a função len(), contando a partir do 0
print(len(nome))

#para saber a posição qu um caracter ocupa