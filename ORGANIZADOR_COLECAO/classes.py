class Pessoa:
    def __init__(self,nome,cpf,email):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email

    def dados(self):
        return {self.__cpf:{'NOME':self.__nome,'E-MAIL':self.__email}}

class Aluno:
    def __init__(self,pessoa):
        self.__pessoa = pessoa.dados()
        self.__pessoa['MAT'] = []
        print(self.__pessoa)

    def matricula(self,mat):
        self.__pessoa['MAT'].append(mat)
        print(self.__pessoa)
        return self.__pessoa