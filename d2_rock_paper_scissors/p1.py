def read_input(path):
    with open(path, 'r') as f:
        inp = f.readlines()
    return [k.strip().split(' ') for k in inp]


def outcome_score(moves):
    if moves[0] == 'A':
        if moves[1] == 'X':
            return 3
        if moves[1] == 'Y':
            return 6
        if moves[1] == 'Z':
            return 0

    if moves[0] == 'B':
        if moves[1] == 'Y':
            return 3
        if moves[1] == 'Z':
            return 6
        if moves[1] == 'X':
            return 0

    if moves[0] == 'C':
        if moves[1] == 'Z':
            return 3
        if moves[1] == 'X':
            return 6
        if moves[1] == 'Y':
            return 0

def moves_score(moves):
    base = ord('X')-1
    shape_score = ord(moves[1]) - base
    return shape_score + outcome_score(moves)

def simulate_strategy(moves_list):
    moves_scores = [moves_score(m) for m in moves_list]
    return sum(moves_scores)

if __name__=="__main__":
    path = './input.txt'
    # path = './test_input.txt'
    inp = read_input(path)
    answer = simulate_strategy(inp)
    print(answer)