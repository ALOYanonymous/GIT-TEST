'''def omnitrix():
    name = input('Qual seu nome? ')
    print(f'Olá Sr. {name}!')

def sistema_de_voz():
    tipo_de_voz = input('Você prefere uma voz do sexo semelhante ou oposto? ')
    print(f'Voz do tipo {tipo_de_voz} definida como padrão.')

def recalibragem():
    print(f'O omnitrix iniciou o modo de recalibragem Sr. {name}, não se desespere, novos DNA´s alienigenas serão desbloqueados em breve!')

def recalibrad_omnitrix():
    contato = input(')( ')
    if contato == 'Entrar em contato com Azimulth':
        print('Olá garoto!')
    else:
        print('O Azimulth não esta disponivel no momento.')

def colocando_o_omnitrix():
    omnitrix()
    sistema_de_voz()
    recalibragem()
    recalibrad_omnitrix()

colocando_o_omnitrix('')

def soma(x,y,z):
    return x + y + z

soma = soma(2,2,2)
print(soma)'''

def maior_número():
    num = input('Digite quantos números desejar: ')
    num = list(map(int, num.split(' ')))
    print(num)
    num.sort()
    print(num)
    num.reverse()
    print(num)
    maior_número =  num[0]
    return maior_número

resultado = maior_número()
print(resultado)