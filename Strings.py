nome = input('Insira o seu nome aqui... ')
print('Seu nome maíusculo: %s' % nome.upper())
print('Minúsculo: %s' % nome.lower())
print('Seu nome tem', len(nome) - nome.count(' '), 'letras')
print('Seu primeiro nome possui', len(nome.split()[0]), 'letras')