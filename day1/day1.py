import re
import pdb
def main():

    coords = []

    with open('input.txt') as f:
        data = f.readlines()
    
    for line in data:
        coords.append(extract_coords(line))

    print(sum(coords))
    
def extract_coords(
        line : str
) -> int:
    pattern = re.compile(r'\d')
    match = pattern.findall(line)
    if match is not None:
        if len(match)>1:
            return int(match[0] + match[-1])
        elif len(match) == 1:
            return int(match[0] + match[0])
    return 0


if __name__ == '__main__':
    main()