from objetos import LISTA 

# Arquivo utilizado para demonstrar a utilização do objeto e seus métodos

# Criando uma lista aleatória com os parâmetros estabelecidos (tamanho, valor minimo, valor máximo)
var = LISTA(10,1,10)

# Utilizando o métodos de exibir a lista criada anteriormente e guardando o valor que retorno para uso posterior
var2 = var.EXIBIR_LISTA()

# Ordenando a lista do objeto utilizando de parâmetro o método de ordenação que desejo utilizar
var('bubble')

# Exibindo a lista já ordenada e salvando a mesma com nome padrão, o nome do arquivo é um parâmetro opcional
var.EXIBIR_LISTA()
var.SALVAR()

# Utilizando o valor da lista salvo anteriormente para chamar de método público com o nome do algoritmo que quero utilizar 
var3 = LISTA.SELECTION(var2)
print(var3)
