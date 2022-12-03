def read_input(path):
    with open(path, 'r') as f:
        inp = f.readlines()
    return [(k[:len(k)//2],k[len(k)//2:]) for k in inp]

def find_overlaps(rucksacks):
    overlaps = []
    for compartment1, compartment2 in rucksacks:
        overlaps.append(list(set(compartment1).intersection(set(compartment2)))[0])
    return overlaps

def overlap_char_to_priority(char):
    # distinguish between upper/lowercase because they're not contiguos
    if char.isupper():
        base = ord('A')-1 - 26 # add 26 because lowercase chars take the first 25
    elif char.islower():
        base = ord('a')-1
    return ord(char) - base

if __name__=='__main__':
    path = './input.txt'
    # path = './test_input.txt'
    rucksacks = read_input(path)
    overlaps = find_overlaps(rucksacks)
    print(overlaps)
    answer = sum([overlap_char_to_priority(k) for k in overlaps])
    print(answer)


