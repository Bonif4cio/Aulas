nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
if idade >= 18:
    print('Cadastro permitido.')
else:
    print('Cadastro negado.')

saldo = float(input('Digite seu saldo:'))
saque = float(input('Valor do saque:'))
if saque <= saldo:
    print('Transacao aceita')
else:
    print('Transacao negada.')