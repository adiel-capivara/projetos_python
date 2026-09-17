#variáveis guardam valores que podem ser alterados durante a execução do programa. Elas são usadas para armazenar dados temporários,
#como números, textos ou objetos, que podem ser manipulados e utilizados em diferentes partes do código.

custo = 1000
faturamento = 1100
novas_vendas = 500

print('custo', custo)
print('faturamento', faturamento + novas_vendas)
print('lucro', (faturamento + novas_vendas) - custo)

#tipos de variáveis

#números inteiros (int), transforma em numúmeros sem casa decimal
preco = int(50)

#números com casa decimal (float), usa ponto devido o padrão internacional
acrescimo = 0.5

#textos (strings, str), usa aspas simples ou duplas
empresa = 'superPress'

#booleanos (bool) - True ou False
teve_lucro = True



#operadores especiais

#mod (%), resto da divisão
print('resto da divisão', 10 % 3)

#floor division (//), retorna a parte inteira da divisão
print('divisão inteira', 10 // 3)