#Definindo uma coleção: set{}
steven_universe = {'Garnet', 'Pearl', 'Amethyst'}

#A função .add() esta adicionando um novo valor a coleção: set{}
steven_universe.add('Peridot')

#A função .remove() esta removendo um valor em especifico da coleção: set{}
steven_universe.remove('Amethyst')

#A função .pop() irá remover o ultimo valor de uma coleção
steven_universe.pop()

#A função print() irá imprimir o que foi solicitado pelo usuário, na tela
print(steven_universe)
                                                    #Trabalhando com a coleção: set{}
#///////////////////////////////////////////////////////////////////////////////////

#Definindo uma coleção: dictionary{}
relógio = {
    '01:00' : '13:00',
    '02:00' : '14:00',
    '03:00' : '15:00',
    '04:00' : '16:00',
    '05:00' : '17:00',
    '06:00' : '18:00',
    '07:00' : '19:00',
    '08:00' : '20:00',
    '09:00' : '21:00',
    '10:00' : '22:00',
    '11:00' : '23:00',
    '12:00' : '00:00'
}

#A função print() irá imprimir o que foi solicitado pelo usuário, na tela
print(relógio)

#A função print() em conjunto com nome do dicionário irá imprimir o valor da chave solicitada pelo usuário, na tela
print(relógio['05:00'])

#Basicamente a função .get() é quase a mesma coisa da função a cima, uma diferença é que ela não irá dar erro se tiver uma função que não exista, exibindo: "None" na tela
print(relógio.get('07:00'))

#Na função .get() também, se você inserir dois parâmetros estará definindo um valor padrão para a primeira "chave" criada por você na mesma função
print(relógio.get('Alimento', 'Arroz'))

#A função len() indicará a quantidade de resultados presente no dicionário
print(len(relógio))
                                             #Trabalhando com a coleção: dictionary{}
#///////////////////////////////////////////////////////////////////////////////////