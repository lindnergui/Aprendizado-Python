from time import sleep

def contador(inicio, fim, passo):
    print(inicio, 'até', fim, 'de', passo, 'em', passo)
    if passo < 0:
       passo = abs(passo)
    if passo == 0:
       passo = 1
    if inicio > fim:
        passo = -passo
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(f'  {i}', end=' ', flush=True)
    elif inicio > fim:
        for i in range(inicio, fim - 1, passo):
            sleep(0.5)
            print(f'  {i}', end=' ', flush=True)
    print('FIM')
    print('-'*50)
contador(1, 10, 1)
contador(10, 1, 1)
contador(inicio=int(input('Digite o início: ')), 
    fim=int(input('Digite o fim: ')), 
    passo=int(input('Digite o passo: ')))