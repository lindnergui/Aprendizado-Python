def maior(* num):
    if not num:
        print('Nenhum número foi encontrado')
    else:
        print('O maior número é', max(num))
maior(1, 4, 8, 4, 9, 2)
print('-'*50)
maior(2, 4, 3, 1)
print('-'*50)
maior(1, 3)
print('-'*50)
maior()
