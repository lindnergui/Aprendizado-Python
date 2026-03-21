n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2)/2
print(f'A sua nota foi {m:.1f}')
if m >= 6:
    print('Média muito boa')
else:
    print('Estude')