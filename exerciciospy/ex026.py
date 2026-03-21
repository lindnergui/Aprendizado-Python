frase = str(input('Digite uma frase ')).strip()
letraa = frase.lower().count ('a')
primeiroa = frase.find('a') + 1
ultimoa = frase.rfind('a') + 1
print('Sua frase tem a letra A {} vezes'.format(letraa))
print('O "A" apareceu na frase pela primeira vez na posição {}'.format(primeiroa))
print('O "A" apareceu pela última vez na posição {}'.format(ultimoa))