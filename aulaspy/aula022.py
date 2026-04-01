def ParOuImpar(num = 1):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

f1 = ParOuImpar(5)
f2 = ParOuImpar(4)
f3 = ParOuImpar()
print(f'Os resultados são: {f1}, {f2}, {f3}')