# Problema A 
# O Bruxo e os Frascos

def conta_vogal(texto):
  vogais = 'aeiouAEIOU'
  contagem = 0
  
  for letra in texto:
    if letra in vogais:
      contagem += 1
    
  return contagem % 3

     
nome= input("Digite o nome: ")
vogais = conta_vogal(nome)
print(f"frasco {vogais}")

  
  