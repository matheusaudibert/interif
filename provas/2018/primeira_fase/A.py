# Problema A
# Funções Matemáticas

# Exemplos de Entradas  Exemplos de Saídas 
# 5 3    Beto ganhou 

# 2 30   Carlos ganhou 

# 2 100  Carlos ganhou 

# 30 20  Beto ganhou  

# 15 5   Rafael Ganhou 


x,y=map(int,input().split())
valores={'Rafael':(3*x)**2+y**2,'Beto':2*x**2+(5*y)**2,'Carlos':-100*x+y**3}
ganhador=max(valores,key=valores.get)
print(f'{ganhador} ganhou')

