# Problema A
# Funções Matemáticas

# Exemplos de Entradas  Exemplos de Saídas 
# 5 3    Beto ganhou 
# 2 30   Carlos ganhou 
# 2 100  Carlos ganhou 
# 30 20  Beto ganhou  
# 15 5   Rafael Ganhou 


# Lê dois valores inteiros da entrada, separados por espaço, e os atribui a x e y.
x,y=map(int,input().split())
# Cria um dicionário para armazenar o resultado das funções de cada competidor.
# A chave é o nome do competidor e o valor é o resultado do cálculo da sua função específica.
valores={'Rafael':(3*x)**2+y**2,'Beto':2*x**2+(5*y)**2,'Carlos':-100*x+y**3}
# Encontra o competidor (chave do dicionário) que possui o maior valor.
# A função max() usa 'valores.get' como chave de comparação, ou seja, compara os valores do dicionário.
ganhador=max(valores,key=valores.get)
# Imprime o nome do ganhador formatado na string de saída.
print(f'{ganhador} ganhou')

