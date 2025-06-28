a=float(input())
b=float(input())
c=float(input())

if a == b or a == c or b == c:
    print('Empatou')
else:
  distancias={'Equipe C':a,'Equipe D':b,'Equipe E':c}
  ganhador=min(distancias, key=distancias.get)
  print(f'{ganhador} ganhou')
