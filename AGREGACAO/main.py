from classes import *

# Criação de um objeto pessoa que é construída com Nome, Cpf e um email
pessoa1 = Pessoa('Joao','123.456.678-90','email@email.com')
print(pessoa1._dados())

# Agregação do objeto Pessoa ao Objeto aluno que herda os valores previamente estabelecidos no objeto pessoa
aluno1 = Aluno(pessoa1)
print(aluno1._dados())

# Por sua vez o objeto Aluno tem o método para adicionar uma nova informação ao objeto pessoa, nesse caso a matrícula
aluno1.matricula('01')
print(aluno1._dados())

# Um mesmo aluno pode receber diversas matrículas (abstração de reingresso ou mudança de curso)
aluno1.matricula('02')
print(aluno1._dados())

# Não é possível adicionar uma matrícula repetida a um mesma pessoa
aluno1.matricula('02')
print(aluno1._dados())

# O objeto aluno pode receber como parâmetro um outro objeto aluno anteriormente instanciado na memória, afinal, o objeto pessoa e o objeto aluno tem as mesmas propriedades, será retornardo uma msg dizendo que o aluno já é cadastrado
aluno2 = Aluno(aluno1)
print(aluno2._dados())

# Porém, para evitar redundância, os dois objetos agregados e repetidos recebem a mesma mudança, sendo assim prossível alterar qualquer um dos dois e receber o mesmo resultado
aluno1.matricula('03')
aluno2.matricula('04')

print(aluno1._dados())
print(aluno2._dados())