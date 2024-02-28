valor = float(input('Insira o valor a ser depositado R$'))
rendimento = float(input('Insira o rendimento em porcentagem anual: '))
anos = int(input('Insira por quantos anos você quer deixar o dinheiro parado: '))

calculo = valor * (rendimento / 100) * anos
valor_bruto = valor + calculo

print(f'\nO valor bruto após {anos} anos é de R${valor_bruto:.2f}')
print(f'O rendimento acumulado nesse periodo é de R${calculo:.2f}')
