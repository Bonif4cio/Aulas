if True:
    print('condicao verdadeira')

idade = 16
if idade < 18:
    print('Menor de Idade.')

if True:
    print('Verdade')
else:
    print('Falso')

idade = 15
if idade >= 18:
    print('Você pode Dirigir.')
else:
    print('Nao pode Dirigir.')

numero = 12
if numero > 10:
    print('maior que 10')
else:
    print('O numero é menor que 10.')

temperatura = float(input('Digite a temperatura:'))

if temperatura >= 30:
    print('Esta muito calor.')
else:
    print('Esta suave.')

numero = int(input('Digite um numero:'))
if numero > 50:
    print('Parabens')

nota = float(input('Digite sua nota:'))
if nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')

numero = int(input('Digite um numero:'))
if numero > 0:
    print('Numero positivo!')

numero = int(input('Digite sua idade:'))
if numero >= 16:
    print('Pode votar')
else:
    print('Nao pode votar.')

numero = int(input('Digite um numero:'))
if numero < 0:
    print('Menor que 0')
else:
    print('Maior que 0')

preco = float(input('Digite o preço do produto:'))
if preco > 100:
    print('Desconto de 10% aplicado!')

salario = float(input('Digite seu salario:'))
if salario > 2.500:
    print('Paga imposto')
else:
    print('Nao paga imposto.')

numero = int(input('Digite um numero'))
if(numero)%5 == 0:
    print('multiplo de 5')