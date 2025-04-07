usuario = input('digite seu login:')
senha = input('digite sua senha:')

if usuario == ('Bonifacio') and senha == ('3077'):
    print('Acesso permitido!')

elif senha != ('3077'):
    print('senha ou usuario invalidos')
elif usuario != ('Bonifacio'):
    print('usuario ou senha invalidos.')


filmes = input('digite o genero do filme:')
if filmes == 'terror':
    print('invocação do mal')
elif filmes == 'comedia':
    print('gente grande')
elif filmes == 'ação':
    print('tropa de elite')
elif filmes == 'suspense':
    print('fuja')
elif filmes == 'romance':
    print('a cinco passos de voce')
else:
    print('filmes nao encontrados.')





