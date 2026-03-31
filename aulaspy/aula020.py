def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6 ,4 ,7 ,2 ,9, 8]
dobra(valores)
print(valores)

