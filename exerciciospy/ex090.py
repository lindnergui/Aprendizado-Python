aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print(f'O aluno {aluno['nome']} tem media {aluno['media']} e portanto está {aluno['situacao']}')