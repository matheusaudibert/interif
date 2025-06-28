def parse_throws(throws_str):
    """Converte a string de arremessos em uma lista de inteiros."""
    scores = []
    for char in throws_str:
        if char == 'X':
            scores.append(10)
        else:
            scores.append(int(char))
    return scores

def calculate_score(throws):
    """Calcula a pontuação de boliche a partir de uma lista de arremessos."""
    frame_scores = []
    throw_index = 0
    
    # Calcula a pontuação para os primeiros 9 frames
    for frame in range(9):
        # Strike
        if throws[throw_index] == 10:
            frame_score = 10 + throws[throw_index + 1] + throws[throw_index + 2]
            frame_scores.append(frame_score)
            throw_index += 1
        # Spare
        elif throws[throw_index] + throws[throw_index + 1] == 10:
            frame_score = 10 + throws[throw_index + 2]
            frame_scores.append(frame_score)
            throw_index += 2
        # Frame normal
        else:
            frame_score = throws[throw_index] + throws[throw_index + 1]
            frame_scores.append(frame_score)
            throw_index += 2

    # Calcula a pontuação para o 10º frame
    tenth_frame_score = 0
    while throw_index < len(throws):
        tenth_frame_score += throws[throw_index]
        throw_index += 1
    frame_scores.append(tenth_frame_score)
    
    return frame_scores

def main():
    """Função principal para rodar o programa do placar de boliche."""
    try:
        num_competitors = int(input())
    except (ValueError, EOFError):
        return

    players_data = []

    for _ in range(num_competitors):
        name = input()
        throws_str = input()
        
        throws = parse_throws(throws_str)
        frame_scores = calculate_score(throws)
        
        cumulative_scores = []
        total_score = 0
        for score in frame_scores:
            total_score += score
            cumulative_scores.append(total_score)
            
        players_data.append({
            "name": name,
            "cumulative_scores": cumulative_scores,
            "total_score": total_score
        })

    # Ordena os jogadores: primeiro por pontuação (decrescente), depois por nome (alfabética)
    players_data.sort(key=lambda p: (-p["total_score"], p["name"]))

    # Exibe os resultados
    for player in players_data:
        scores_str = "".join([f"|{s}" for s in player["cumulative_scores"]])
        print(f'{player["name"]} : {scores_str}| Total = {player["total_score"]}')

if __name__ == "__main__":
    main()