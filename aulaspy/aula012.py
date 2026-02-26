nome = str(input('Digite seu nome'))
if nome == 'Guilherme':
    print('Que lindo nome você tem')
elif nome == 'Pedro'or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é muito popular no Brasil')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Nossa que nome normal')
print(f'Bom dia {nome}')