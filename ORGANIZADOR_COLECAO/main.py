from classes import *
# 'jose','123.456.678-90','email@email.com','00000000'

pessoa1 = Pessoa('jose','123.456.678-90','email@email.com')

print(pessoa1._dados())
aluno1 = Aluno(pessoa1)
print(aluno1._dados())
aluno1.matricula('01')
print(aluno1._dados())
aluno1.matricula('02')
print(aluno1._dados())
aluno2 = Aluno(aluno1)
print(aluno2._dados())
aluno2.matricula('03')
print(aluno1._dados())
print(aluno2._dados())