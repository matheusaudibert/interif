# Problema A 
# O Bruxo e os Frascos

# Exemplos de Entradas  Exemplos de Saídas
# Manticora             # frasco 1 
  
# Grifo                 # frasco 2 
  
# Dragao Fofao          # frasco 0 
  
# Liche bondoso bacanA  # frasco 2

def conta_vogal(texto):
  vogais = 'aeiouAEIOU'
  contagem = 0
  for letra in texto:
    if letra in vogais:
      contagem += 1
  return contagem % 3
nome = input()
vogais = conta_vogal(nome)
print(f"frasco {vogais}")

  
  