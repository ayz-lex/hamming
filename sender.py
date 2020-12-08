import numpy as np

generator_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1]
])

def generate(string: str):
    v = np.array([int(s) for s in string])

    result = generator_matrix @ v

    result %= 2

    return ''.join([str(char) for char in result])

print('Enter a bit string with a length that is a multiple of 4: ')

inp = input()

while True:
    if len(inp) % 4 == 0:

        if not inp:
            break

        i = 0
        while i < len(inp):
            char = inp[i]
            if char != "0" and char != "1":
                print('')
                break
            i += 1
        
        if len(inp) == i:
            break
        else:
            print('The input is not a bit string. The only characters should be 0 or 1. Please reenter: ')
            inp = input()

    else:
        print('The given input doesn\'t have a length that is a multiple of 4, please reenter: ')
        inp = input()

output = ""
start = 0
while start < len(inp):
    curSection = inp[start: start + 4]

    output += generate(curSection)
    start += 4

print(f"\nThe encoded bit string is the following:\n{output}")