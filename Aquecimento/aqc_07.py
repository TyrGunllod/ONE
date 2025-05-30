#7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose
#em um banco de dados e gostaria de rotular os dados da seguinte maneira:

#Glicose igual ou inferior a 70: 'Hipoglicemia'
#Glicose entre 70 a 99: 'Normal'
#Glicose entre 100 e 125: 'Alterada'
#Glicose superior a 125: 'Diabetes'
#A clínica disponibilizou parte dos valores e sua tarefa
#é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor
#da glicemia em cada tupla.


glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92,
            66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

#Minha solução
classificacao = [
    'Hipoglicemia' if valor < 70 else
    'Normal' if valor < 100 else
    'Alterada' if valor < 126 else
    'Diabetes'
    for valor in glicemia
]

rotulo = [tup for tup in zip(classificacao, glicemia)]
print(rotulo)
print('')

#Instrutor
rotulos = [('Hipoglicemia', glicose) if glicose <= 70 else
           ('Normal', glicose) if glicose < 100 else
           ('Alterada', glicose) if glicose < 125 else
           ('Diabetes', glicose) for glicose in glicemia]
print(rotulos)
