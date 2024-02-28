anime = True

if anime:
    print('Passed')
else:
    print('Fail')

pastor_alemão = True
doberman = False

if pastor_alemão or doberman:
    print('Vou passear!')
else:
    print('Vou ficar em casa!')

anime_echi = True
internet = True

if anime_echi and internet:
    print('Vou assistir!.')
else:
    print('Vou ficar codando')

celular = 0
console = 1
volante = 0

if celular and console:
    print('Vai puta, vou conseguir jogar Gram Turismo!')

elif celular and not console:
    print('Dá pro gasto né (kkk).')

elif not celular and console:
    if volante:
        print('Agora ficou melhor do nunca!')
    else:
        print('Agora sim o bixo vai pegar (kkk).')

else:
    print('Só me resta assistir mesmo!')

n1 = 7
n2 = 5

if n1 == n2:
    print(f'{n1} é igual a {n2}')

#elif n1 != n2:
    print(f'{n1} é diferente de {n2}')

#elif n1 > n2:
    print(f'{n1} é maior que {n2}')

elif n1 < n2:
    print(f'{n1} é menor que {n2}')

elif n1 >= n2:
    print(f'{n1} é maior ou igual a {n2}')

elif n1 <= n2:
    print(f'{n1} é menor ou igual a {n2}')