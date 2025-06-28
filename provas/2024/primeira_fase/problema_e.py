def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def esta_dentro(polygon, px, py):
    n = len(polygon)
    sinal = None

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % n]  # próximo vértice

        # Vetor da aresta
        vx = x2 - x1
        vy = y2 - y1

        # Vetor do ponto para o primeiro vértice
        ux = px - x1
        uy = py - y1

        cp = cross(vx, vy, ux, uy)

        if cp != 0:
            if sinal is None:
                sinal = cp > 0
            elif (cp > 0) != sinal:
                return False

    return True

# Entrada
n = int(input())
poligono = [tuple(map(int, input().split())) for _ in range(n)]
px, py = map(int, input().split())

# Verificação
if esta_dentro(poligono, px, py):
    print("DENTRO")
else:
    print("FORA")
    
# IA QUE FEZ ESSA MERDA