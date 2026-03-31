lar = float(input('Digite a largura de sua parede'))
alt = float(input('Digite a altura da parede'))
area = lar*alt
print('A área de sua parede é de {}m²'.format(area))
print('A tinta necessária para sua parede de {}m² é {:.2f}L'.format(area, area/2))
