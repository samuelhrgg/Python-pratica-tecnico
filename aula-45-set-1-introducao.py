"""
Estruturas de dados: SET { }
A estrutura de dados set em Python é uma coleção não ordenada de
elementos únicos. É semelhante a uma lista ou um dicionário, mas com
algumas características distintas que a tornam particularmente útil 
em várias situações.

Características do set

Elementos únicos: Um set não permite elementos duplicados. Cada elemento 
deve ser único.

Não ordenado: Os elementos em um set não têm uma ordem específica. 
Quando você percorre um set, a ordem dos elementos pode não ser a mesma 
em que foram adicionados.

Mutável: Você pode adicionar ou remover elementos de um set após
sua criação.

Criando um set
Você pode criar um set usando chaves { } ou a função set( ):

meuSet = {1,2,3,4}
meuSet = set([1,2,3,4,5])

"""
#Criando um set
s1 = set()
print(s1,type(s1))

#Colocando um iterável
s2 = set('Samuel')
print(s2)

#set direto com elementos
s3 = {'samuel',2,3}
print(s3)

#sem valores iguais
s4 = {2,3,4,5,5,5,6,2,0,True,False}
print(s4)

"""
Estruturas de dados: Aplicações com SET { }

Remoção de Duplicatas: sets são usados para remover duplicatas de uma 
lista de itens. Por exemplo, ao lidar com listas de clientes ou transações,
um set pode ajudar a garantir que cada entrada seja única.

Operações de Conjunto: Em análises de dados e ciências de dados, 
operações como união, interseção e diferença são comuns. Por exemplo,
ao comparar grupos de clientes que compraram diferentes produtos.

Busca Eficiente: A busca em um set é, em média, mais rápida do que em listas,
pois sets são implementados usando tabelas hash*. Isso é útil em situações
onde verificações de associação rápidas são necessárias.

Análise de Redes Sociais: Em análises de redes sociais, como verificar amigos
em comum entre dois usuários ou seguidores exclusivos de um usuário.

Filtragem de Dados: Quando se precisa filtrar dados com base em critérios
complexos de inclusão/exclusão, os sets tornam as operações mais rápidas e simples.

* Uma tabela hash é uma estrutura de dados que mapeia chaves para valores, 
permitindo acesso rápido aos dados. É usada para implementar arrays associativos
ou dicionários, onde você pode armazenar pares de chave-valor e recuperar valores
eficientemente usando suas chaves.


"""