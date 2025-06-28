# Problema F
# Jogando Bocha

# Exemplos de Entrada  Exemplos de Saída
# 19.5  # Equipe C ganhou
# 22.4
# 24.2

# 20.4  # Equipe A ganhou
# 19.1
# 17.9

# 12.9  # Equipe C ganhou 
# 18.1
# 23.1

# 12.9  # Empatou
# 18.1
# 18.1

a=float(input())
b=float(input())
c=float(input())
if a==b or a==c or b==c:
    print('Empatou')
else:
  distancias={'Equipe C':a,'Equipe D':b,'Equipe E':c}
  ganhador=min(distancias,key=distancias.get)
  print(f'{ganhador} ganhou')
