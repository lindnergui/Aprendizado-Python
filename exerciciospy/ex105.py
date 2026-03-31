
def notas(* num, sit=False):

    """
    -> Função para analisar notas e situação de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    d = dict()
    d['Total'] = len(num)
    d['Maior'] = max(num)
    d['Menor'] = min(num)
    d['Media'] = sum(num) / len(num)
    if sit:
        if d['Media'] >= 7:
            d['Situação'] = 'BOA'
        elif d['Media'] >= 5:
            d['Situação'] = 'RAZOAVEL'
        else:
            d['Situação'] = 'RUIM'
    return d

print(notas(5.5, 9.5, 10, 6.5, 3, 8.4, sit=False))

print(notas(5.5, 9.5, 10, 6.5, sit=True))
help(notas)

