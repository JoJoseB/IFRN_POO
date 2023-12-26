# AGREGAÇÃO
Este documento tem como objetivo explicar o conceito de agregação em Programação Orientada a Objetos (POO) utilizando um exemplo em Python. A agregação é uma das formas de estabelecer relações entre objetos em POO, onde um objeto pode conter ou ser composto por outros objetos. No exemplo, temos duas classes: Pessoa e Aluno, que demonstram a relação de agregação.

## Classe Pessoa
A classe Pessoa representa uma pessoa com atributos como nome, CPF e email. Esta classe também possui um método _dados() que retorna um dicionário com os dados da pessoa, onde o CPF é a chave e os valores são um dicionário contendo nome e email.

## Classe Aluno
A classe Aluno é outra classe que representa um aluno, e ela faz uso de agregação para incluir uma instância da classe Pessoa como um de seus atributos. Um objeto do tipo Pessoa é passado como argumento, e seus dados são armazenados na instância de Aluno. Isso é um exemplo de agregação, onde a classe Aluno "tem" um objeto da classe Pessoa.

### CONSIDERAÇÕES
A agregação é útil quando você deseja criar objetos complexos que são compostos por outros objetos menores e reutilizáveis. No exemplo acima, um aluno é uma pessoa com informações adicionais relacionadas à matrícula, que podem ser adicionadas e acessadas através dos métodos da classe Aluno, como matricula(). A classe Aluno pode acessar os dados da classe Pessoa através do atributo self.__pessoa, demonstrando a relação de agregação. Esse é apenas um exemplo simples de como a agregação pode ser usada em POO em Python. Ela permite criar estruturas de objetos mais complexas e modulares, melhorando a organização e reutilização do código.

---

# AGGREGATION

This document aims to explain the concept of aggregation in Object-Oriented Programming (OOP) using an example in Python. Aggregation is one way to establish relationships between objects in OOP, where an object can contain or be composed of other objects. In the example, we have two classes: Person and Student, demonstrating the aggregation relationship.

## Person Class

The Person class represents a person with attributes such as name, CPF, and email. This class also has a method _data() that returns a dictionary with the person's data, where CPF is the key, and the values are a dictionary containing name and email.

## Student Class
The Student class is another class that represents a student, and it uses aggregation to include an instance of the Person class as one of its attributes. An object of type Person is passed as an argument, and its data is stored in the instance of Student. This is an example of aggregation, where the Student class "has" an object of the Person class.
### CONSIDERATIONS

Aggregation is useful when you want to create complex objects composed of smaller and reusable objects. In the example above, a student is a person with additional information related to enrollment, which can be added and accessed through the methods of the Student class, such as enrollment(). The Student class can access the data of the Person class through the attribute self.__person, demonstrating the aggregation relationship. This is just a simple example of how aggregation can be used in OOP in Python. It allows creating more complex and modular object structures, improving code organization and reusability.