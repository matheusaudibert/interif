# Problema I
# Conversando em segredo

# Exemplos de entrada  Exemplos de Saída
# 1 institutofederal chaveaseutilizar  # fvrpdubytzvpvrzd
# 2 ozysnssvpt outrachave              # desaopaulo
# 0

def cifrar_mensagem(frase,senha):
    resultado=''
    for i in range(len(frase)):
      if i%2!=0:
        resultado+=letra_soma(frase[i],senha[i])
      else:
        resultado+=letra_subtracao(frase[i],senha[i])
    return resultado

def decifrar_mensagem(frase_cifrada,senha):
    resultado=''
    for i in range(len(frase_cifrada)):
        if i%2==0:
            resultado+=letra_soma(frase_cifrada[i],senha[i])
        else: 
            resultado+=letra_subtracao(frase_cifrada[i],senha[i])
    return resultado

def letra_soma(letra1,letra2):
    pos1=ord(letra1.lower())-ord('a')+1
    pos2=ord(letra2.lower())-ord('a')+1

    resultado=(pos1+pos2)%26
    if resultado==0:
        resultado=26
    return chr(ord('a')+resultado-1)
  
def letra_subtracao(letra1,letra2):
    pos1=ord(letra1.lower())-ord('a')+1
    pos2=ord(letra2.lower())-ord('a')+1
    resultado=pos1-pos2
    if resultado<=0:
        resultado+=26
    return chr(ord('a')+resultado-1)

comando=''
while comando!='0':
  texto=input().split()
  comando=texto[0]
  if comando=='0':
    break
  frase=texto[1]
  senha=texto[2]
  if comando=='1':
    print(cifrar_mensagem(frase,senha))
  elif comando=='2':
    print(decifrar_mensagem(frase,senha))