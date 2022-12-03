def read_input(path):
    with open(path, 'r') as f:
        inp = f.readlines()
    return [k.strip().split(' ') for k in inp]


def compute_shape_score(moves):
    if moves[0] == 'A':
        if moves[1] == 'X':
            return 3
        if moves[1] == 'Y':
            return 1
        if moves[1] == 'Z':
            return 2

    if moves[0] == 'B':
        if moves[1] == 'X':
            return 1
        if moves[1] == 'Y':
            return 2
        if moves[1] == 'Z':
            return 3

    if moves[0] == 'C':
        if moves[1] == 'X':
            return 2
        if moves[1] == 'Y':
            return 3
        if moves[1] == 'Z':
            return 1

def moves_score(moves):
    shape_score = compute_shape_score(moves)
    if moves[1] == 'X':
        outcome_score = 0
    elif moves[1] == 'Y':
        outcome_score = 3
    elif moves[1] == 'Z':
        outcome_score = 6

    return shape_score + outcome_score

def simulate_strategy(moves_list):
    moves_scores = [moves_score(m) for m in moves_list]
    return sum(moves_scores)

if __name__=="__main__":
    path = './input.txt'
    # path = './test_input.txt'
    inp = read_input(path)
    answer = simulate_strategy(inp)
    print(answer)