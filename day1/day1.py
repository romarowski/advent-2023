import re
import pdb
def main():

    coords = []

    with open('input.txt') as f:
        data = f.readlines()
    
    for line in data:
        coords.append(extract_coords(line))

    with open('output.txt', 'w') as f:
        # write out the list of coords each on a new line
        for coord in coords:
            f.write(str(coord) + '\n')


    print(sum(coords))
    
def extract_coords(
        line : str
) -> int:
    options = ['one', 'two', 'three', 'four', 
                'five', 'six', 'seven', 'eight', 
                'nine']
    pos_pattern = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d')   
    neg_pattern = r''
    for opt in options:
        neg_pattern += opt[::-1] + '|'
    neg_pattern += r'\d'
    pos_match = pos_pattern.findall(line)
    neg_pattern = re.compile(neg_pattern)
    neg_match = neg_pattern.findall(line[::-1])
    map_ = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    if pos_match is not None:
        n1 = pos_match[0]
        if n1 in map_.keys():
            n1 = map_[n1]
    if neg_match is not None:
        n2 = neg_match[0]
        if n2[::-1] in map_.keys():
            n2 = map_[n2[::-1]]
    if n1 is not None and n2 is not None:
        return int(n1 + n2)
    return 0


if __name__ == '__main__':
    main()