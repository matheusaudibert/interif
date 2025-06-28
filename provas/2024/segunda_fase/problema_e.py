
n = int(input())

for _ in range(n):
  entrada = input()
  resultado = ""
  codigo = ""
  for letra in entrada:
    if letra.isalpha():
      resultado += letra
    else:
      codigo += letra
      if int(codigo) >= 97 and int(codigo) <= 122:
        resultado += chr(int(codigo))
        codigo = ""
  print(resultado)     
      