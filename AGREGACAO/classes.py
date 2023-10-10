class Pessoa:
    def __init__(self,nome,cpf,email):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
    
    def _dados(self):
        return {self.__cpf:{'NOME':self.__nome,'E-MAIL':self.__email}}

class Aluno:
    def __init__(self,pessoa):
        self.__pessoa = pessoa._dados()
        self.var = list(self.__pessoa.keys())[0]
        print(self.__pessoa[self.var])
        if 'MAT' not in self.__pessoa[self.var]:
            self.__pessoa[self.var]['MAT'] = []
        else:
            print('Aluno já cadastrado')

    def matricula(self,mat):
        if mat in self.__pessoa[self.var]['MAT']:
            print(f'{mat} já associado ao CPF {self.var}')
        else:
            self.__pessoa[self.var]['MAT'].append(mat)
        return self.__pessoa
    
    def _dados(self):
        return self.__pessoa