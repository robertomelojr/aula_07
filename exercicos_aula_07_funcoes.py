## Funções

from typing import List

lista_de_teste : List = [10,10,20,30,40,100,30,40]

print(lista_de_teste)
# Calcular Média de Valores em uma Lista

def calcular_media (lista_de_valores : List) -> float:
    
    """ Função de cálculo de média de valores inseridos em uma lista
    """
    return sum(lista_de_valores)/len(lista_de_valores)

print(calcular_media(lista_de_teste))

# Filtrar Dados Acima de um Limite

lista_filtrada : List = []

def filtragem_de_lista (lista_de_valores : List, valor_inferior : float = 0) -> float:
    
    """ Função que retorna o valor de uma lista de acordo com o parâmetro de valores definido
    """
    for valor in lista_de_valores:
        if valor > valor_inferior:
            lista_filtrada.append(valor)
    
    return(lista_filtrada)


print(filtragem_de_lista(lista_de_teste,30))


#Contar Valores Únicos em uma Lista

def remocao_de_duplicatas_da_lista (lista_de_valores : List) -> float:
  
    """ Função que remove as duplicatas de uma lista e retorna de forma ordenada
    """  
    lista_unica : List = list(set(lista_de_valores))
         
    return(sorted(lista_unica))


print(remocao_de_duplicatas_da_lista(lista_de_teste))

#Converter Celsius para Fahrenheit em uma Lista
lista_de_temperaturas : List = [-45,10,-12,22,32,30,18,22,0]

def converte_para_fahrenheit (lista_de_temperaturas : List) -> float:  
    
    """ Função que converte as temperaturas de Celsius para Fahrenheit e retorna uma lista
    """
    lista_de_temperaturas_convertida : List = [] 
    
    for temperatura in lista_de_temperaturas : 
        
        lista_de_temperaturas_convertida.append(((temperatura * 9/5) + 32))
        lista_de_temperaturas_convertida =  [round(x,2) for x in lista_de_temperaturas_convertida] 
        
    return(lista_de_temperaturas_convertida)

print(converte_para_fahrenheit(lista_de_temperaturas))

#Calcular Desvio Padrão de uma Lista

lista_desvio_padrao : List = [10,22,15,34,75]

def calcular_desvio_padrao(valores: List[float]) -> float:
    
    """ Função que retorna o desvio padrão de uma lista
    """
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

print(calcular_desvio_padrao(lista_desvio_padrao))

#Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    """ Função que retorna os valores ausentes de uma lista
    """
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

lista_sequencia : List =[1,2,4,6,10]

print(encontrar_valores_ausentes(lista_sequencia))