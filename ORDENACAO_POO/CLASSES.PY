import random,os
class LISTA:
    
    # Variaveis privadas
    __lista = None
    __caminho_prog = os.path.dirname(__file__)

    #Métodos privados com os algoritmos de ordenação
    def __bubble(self):
        tam = len(self.__lista)
        for a in range(tam - 1):
            for b in range(tam - 1):
                if self.__lista[b] > self.__lista[a + 1]:
                    self.__lista[b],self.__lista[a + 1] = self.__lista[a + 1], self.__lista[b]
        return self.__lista

    def __insertion(self):
        tam = len(self.__lista)
        for a in range(1, tam):
            num_atual = self.__lista[a]
            b = a - 1
            while b >= 0 and num_atual < self.__lista[b]:
                self.__lista[b+1] = self.__lista[b]
                b -= 1
            self.__lista[b + 1] = num_atual
        return self.__lista

    def __selection(self):
        tam = len(self.__lista)
        for a in range(tam):
            primeira_pos = a
            for b in range(a + 1, tam):
                if self.__lista[b] < self.__lista[primeira_pos]:
                    primeira_pos = b
            self.__lista[a], self.__lista[primeira_pos] = self.__lista[primeira_pos],self.__lista[a]
        return self.__lista

    # Construtor gera lista de números aleatórios com base no valores dados
    def __init__(self,tamanho_lista = 10 ,min_lista = 1,max_lista = 10):
        if tamanho_lista > 0:
            self.__lista = list()        
            for _ in range(tamanho_lista):
                self.__lista.append(random.randint(min_lista, max_lista))
        pass
    
    # Metodo de chamada do objeto sem chamar método
    def __call__(self, ordenacao):
        __sort = {'bubble':self.__bubble,
                'selection':self.__selection,
                'insertion':self.__insertion,
                }
    
        __sort[ordenacao.lower()]()

    def SALVAR(self, nome_arq = 'lista'):
        with open(self.__caminho_prog + '\\' + nome_arq + '.txt','w') as arquivo_a:
            arquivo_a.write(str(self.__lista))
    #####################
    def EXIBIR_LISTA(self):
        print(self.__lista)
        print(self.__caminho_prog)
        return