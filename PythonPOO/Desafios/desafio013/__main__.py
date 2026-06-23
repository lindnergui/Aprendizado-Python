from termostato import *

def main():
    t = Termostato()
    try:
        t.temperatura = 30.4
    except ValueError as e:
        print('Houve um erro: ', e)
    
    print(f'A temperatura atual é: {t.ftemperatura}')


if __name__ == "__main__":
    main()