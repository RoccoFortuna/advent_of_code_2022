def read_input(path):
    with open(path, 'r') as f:
        inp = f.read()
    return [[int(calories) for calories in k.split('\n')] for k in inp.split('\n\n')]

if __name__=="__main__":
    path = "./input.txt"
    # path = "./test_input.txt"
    calories_lists = read_input(path)
    answer = max([sum(k) for k in calories_lists])
    print(answer)