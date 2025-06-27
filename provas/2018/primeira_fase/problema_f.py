# Problema F 
# Pipoqueiro 

# Exemplos de Entrada  Exemplos de Saída 
# 2  12
# 3 
# 4 
  
# 3  10
# 4 
# 2

# Lê os valores de entrada: clientes em cada arquibancada
e1 = int(input())
e2 = int(input())
e3 = int(input())
# Calcula os minutos totais dos trajetos de cada arquibancada
tempo_arq1 = (e2 * 1) + (e3 * 2)
tempo_arq2 = (e1 * 1) + (e3 * 1)
tempo_arq3 = (e1 * 2) + (e2 * 1)
# Pega o menor tempo entre os três trajetos
resultado = min(tempo_arq2, tempo_arq2, tempo_arq2) * 2
# Imprime o resultado
print(resultado)




