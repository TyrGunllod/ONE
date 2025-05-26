#1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

#Minha solução
for i in range(len(lista_de_listas)):
    print(sum(lista_de_listas[i]))

print("")

#Instrutor
for lista in lista_de_listas:
    print(sum(lista))