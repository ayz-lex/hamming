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

input = input()

output = ""
start = 0
while start < len(input):
    curSection = input[start: start + 4]

    output += generate(curSection)
    start += 4

print(f"\nThe encoded bit string is the following:\n{output}")