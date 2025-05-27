#5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista:

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

#Minha solução
despesa_mensal = {mes: val for mes, val in zip(meses, despesa)}
print(despesa_mensal)

print('')

#Instrutor
dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
print(dicionario)