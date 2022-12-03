from p1 import read_input



if __name__=="__main__":
    path = "./input.txt"
    path = "./test_input.txt"
    calories_lists = read_input(path)
    calories_sums = [sum(k) for k in calories_lists]
    answer = sum(sorted(calories_sums)[-3:])
    print(answer)