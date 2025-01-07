
# Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, 
# o desafio consiste em ler os dados, processá-los em um dicionário para análise e, por fim,
# calcular e reportar as vendas totais por categoria de produto.

import csv


def ler_csv(nome_arquivo :str) -> list[dict] :
    
    """Função que lê UM csv e retorna uma lista de dicionário.
    """
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def processar_dados(dados : float):
    
    """Função que retorna os dados processados
    """
    categorias : dict= {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

def calcular_vendas_categoria(dados):
    """Função que realiza o cálculo das vendas por categoria.
    """
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria


def main():
    """Define a main para executar quando estiver rodando em arquivo principal, 
    mas não rodar automaticamente quando for importado como um Lib.
    """
    nome_arquivo = 'vendas.csv'
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)
    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()