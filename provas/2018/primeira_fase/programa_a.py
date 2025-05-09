# Problema A
# Funções Matemáticas

x,y=map(int,input().split())
valores={'Rafael':(3*x)**2+y**2,'Beto':2*x**2+(5*y)**2,'Carlos':-100*x+y**3}
ganhador=max(valores,key=valores.get)
print(f'{ganhador} ganhou')
