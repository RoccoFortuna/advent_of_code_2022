from p1 import read_input
import re
def read_input(path):
    with open(path, 'r') as f:
        inp = f.read()
    inp += '\n'
    three_lines_re = re.compile('[a-zA-Z]+\n[a-zA-Z]+\n[a-zA-Z]+\n')
    return [three_lines.splitlines() for three_lines in three_lines_re.findall(inp)]


def find_overlapping_badge(rucksacks):
    r1, r2, r3 = [set(r) for r in rucksacks]
    overlaps = r1.intersection(r2).intersection(r3)
    return list(overlaps)[0]

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
    overlaps = [find_overlapping_badge(rucksack) for rucksack in rucksacks]
    answer = sum([overlap_char_to_priority(k) for k in overlaps])
    print(answer)


