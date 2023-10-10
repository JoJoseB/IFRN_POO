# AGREGAÇÃO
Este documento tem como objetivo explicar o conceito de agregação em Programação Orientada a Objetos (POO) utilizando um exemplo em Python. A agregação é uma das formas de estabelecer relações entre objetos em POO, onde um objeto pode conter ou ser composto por outros objetos. No exemplo, temos duas classes: Pessoa e Aluno, que demonstram a relação de agregação.

## Classe Pessoa
A classe Pessoa representa uma pessoa com atributos como nome, CPF e email. Esta classe também possui um método _dados() que retorna um dicionário com os dados da pessoa, onde o CPF é a chave e os valores são um dicionário contendo nome e email.

## Classe Aluno
A classe Aluno é outra classe que representa um aluno, e ela faz uso de agregação para incluir uma instância da classe Pessoa como um de seus atributos. Um objeto do tipo Pessoa é passado como argumento, e seus dados são armazenados na instância de Aluno. Isso é um exemplo de agregação, onde a classe Aluno "tem" um objeto da classe Pessoa.

# CONSIDERAÇÕES
A agregação é útil quando você deseja criar objetos complexos que são compostos por outros objetos menores e reutilizáveis. No exemplo acima, um aluno é uma pessoa com informações adicionais relacionadas à matrícula, que podem ser adicionadas e acessadas através dos métodos da classe Aluno, como matricula(). A classe Aluno pode acessar os dados da classe Pessoa através do atributo self.__pessoa, demonstrando a relação de agregação. Esse é apenas um exemplo simples de como a agregação pode ser usada em POO em Python. Ela permite criar estruturas de objetos mais complexas e modulares, melhorando a organização e reutilização do código.





