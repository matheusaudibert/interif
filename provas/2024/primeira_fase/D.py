# Problema D
# Preços de Produtos

# Exemplos de entrada  Exemplos de Saída
# 2 6      # 5

# 20 96    # 89

# 100 400  # 397

def eh_primo(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

a,b=map(int,input().split())
lista=list(range(a,b+1))
primos=[c for c in lista if eh_primo(c)]
print(max(primos))