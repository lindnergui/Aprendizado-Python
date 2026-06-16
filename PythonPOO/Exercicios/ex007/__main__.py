from classes import Aluno, Funcionario, Professor

a1 = Aluno('josé', 17, 'informática', '101')
a1.fazer_aniversario()
a1.Fazer_Matricula()
#inspect(a1)

p1 = Professor('Sameul', 37, 'Biologia', 'Mestrado')
p1.dar_aula()
#inspect(p1)

f1 = Funcionario('Claudia', 27, 'Secretaria', 'Secretaria')
f1.fazer_aniversario()
f1.bater_ponto()
#inspect(f1, methods=True)

a1.estudar()
p1.estudar()
f1.estudar()
