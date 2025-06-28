# Problema A
# Desafio de Lorde Dilon!

# Exemplos de entrada  Exemplos de Saída
# 2    # 3
# 8
# 1
# 2
# 4
# 16
# 21

# 2    # 6
# 4
# 128
# 24

# 2    # frustraka
# 4
# 128
# 15

num_poderes = int(input())
poderes = []
for _ in range(num_poderes):
  poderes.append(int(input()))
magia_necessaria = int(input())
poderes.sort(reverse=True)
soma_magias = 0
possivel = True
qtd = 0
for poder in poderes:
  if magia_necessaria == 0:
    break
  while magia_necessaria >= poder:
      magia_necessaria = magia_necessaria - poder
      soma_magias = soma_magias + 1
if magia_necessaria == 0:
  print(soma_magias)
else:
  print('frustraka')
