import random,os,sys
class LISTA:
    
    # Variaveis privadas
    __lista = None

    # Métodos privados com os algoritmos de ordenação, os algoritmos são:
    #   Bubble sort
    #   Insertion sort
    #   Selection sort
    #   Bogo sort

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

    def __bogo(self):
        while self.__lista != sorted(self.__lista):
            n = len(self.__lista)
            for i in range(0, n):
                r = random.randint(0,n-1)
                self.__lista[i],self.__lista[r] = self.__lista[r],self.__lista[i]
        return self.__lista
    
    # Construtor gera lista de números aleatórios com base no valores dados
    def __init__(self, tamanho_lista:int , min_lista:int, max_lista:int):
        for arg in [tamanho_lista,min_lista,max_lista]:
            if isinstance(arg,int):
                continue
            else:
                raise TypeError(f'{arg} não é do tipo inteiro')
        if min_lista < max_lista:
            self.__lista = list()        
            for _ in range(tamanho_lista):
                self.__lista.append(random.randint(min_lista, max_lista))
        else:
            raise Exception('argumento min_lista deve ser menor que max_lista')
        pass
    
    # Metodo de chamada do objeto sem chamada de método para utilizar os algoritmos na lista criada pelo objeto
    def __call__(self, ordenacao:str):
        if isinstance(ordenacao,str) and ordenacao.capitalize() in ["Bubble","Selection","Insertion"]:
            pass
        else:
            raise TypeError(f'{ordenacao} deve assumir valores "Bubble","Selection","Insertion" ou "Bogo"')
        __sort = {'bubble':self.__bubble,
                'selection':self.__selection,
                'insertion':self.__insertion,
                'bogo':self.__bogo,
                }
        __sort[ordenacao.lower()]()

    # Métodos públicos que recebem uma lista externa e ordena conforme a lista dada nos argumentos e salva em um arquivo externo

    def BUBBLE(lista:list):
        if isinstance(lista,list):
            pass
        else:
            raise TypeError(f'{lista} não é uma lista')
        
        __arq = open('Bubble.txt','w')
        __arq.write(str(lista))
        __arq.close()

        tam = len(lista)
        for a in range(tam - 1):
            for b in range(tam - 1):
                if lista[b] > lista[a + 1]:
                    lista[b],lista[a + 1] = lista[a + 1], lista[b]

        __arq = open('Bubble.txt','a')
        __arq.write(str(lista))
        __arq.close()

        return lista
    
    def INSERTATION(lista:list):
        if isinstance(lista,list):
            pass
        else:
            raise TypeError(f'{lista} não é uma lista')
        
        __arq = open('Insertion.txt','w')
        __arq.write(str(lista))
        __arq.close()
        tam = len(lista)

        for a in range(1, tam):
            num_atual = lista[a]
            b = a - 1
            while b >= 0 and num_atual < lista[b]:
                lista[b+1] = lista[b]
                b -= 1
            lista[b + 1] = num_atual

        __arq = open('Insertion.txt','a')
        __arq.write(str(lista))
        __arq.close()
        return lista

    def SELECTION(lista:list):
        if isinstance(lista,list):
            pass
        else:
            raise TypeError(f'{lista} não é uma lista')
        
        __arq = open('Selection.txt','w')
        __arq.write(str(lista))
        __arq.close()

        tam = len(lista)
        for a in range(tam):
            primeira_pos = a
            for b in range(a + 1, tam):
                if lista[b] < lista[primeira_pos]:
                    primeira_pos = b
            lista[a], lista[primeira_pos] = lista[primeira_pos],lista[a]

        __arq = open('Selection.txt','w')
        __arq.write(str(lista))
        __arq.close()
        return lista
    
    def BOGO(lista:list):
        if isinstance(lista,list):
            pass
        else:
            raise TypeError(f'{lista} não é uma lista')
        
        __arq = open('Bogo.txt','w')
        __arq.write(str(lista))
        __arq.close()

        while lista != sorted(lista):
            n = len(lista)
            for i in range(0, n):
                r = random.randint(0,n-1)
                lista[i],lista[r] = lista[r],lista[i]

        __arq = open('Bogo.txt','w')
        __arq.write(str(lista))
        __arq.close()
        return lista
    
    # Método para exibir a lista criada pelo objeto e um método para salvar em um arquivo externo a lista

    def EXIBIR_LISTA(self):
        print(self.__lista)
        return self.__lista
    
    def SALVAR(self, nome_arq = 'lista'):
        __arq = open(str(nome_arq) + '.txt', 'w')
        __arq.write(str(self.__lista))
        __arq.close()