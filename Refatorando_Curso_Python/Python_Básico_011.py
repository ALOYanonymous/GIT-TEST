#Definindo uma instrução try: em python
try: 
    idade = int(input('Digite a sua idade: '))
    print(idade)
    print(idade/0)

#Ocorre quando você tenta dividir um número por zero
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')

#Ocorre quando você tenta converter um valor de um tipo para outro que não é compatível, como um inteiro para uma string
except ValueError:
    print('Digite um valor válido!')

#Irá retornar "Erro!" pos a instrução "except" captura e manipula os erros
except:
    print('Erro!')

#Essa intrução irá ser executada independentemente de haver ou não um erro no bloco "try:" 
finally:
    print('Foi executado!')