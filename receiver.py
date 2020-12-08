import numpy as np

parity_check_matrix = np.array([
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1]
])

decode_matrix = np.array([
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
])

errorMap = {
    (0, 0, 0): np.array([0, 0, 0, 0, 0, 0, 0]),
    (1, 0, 0): np.array([0, 0, 0, 0, 1, 0, 0]),
    (0, 1, 0): np.array([0, 0, 0, 0, 0, 1, 0]),
    (0, 0, 1): np.array([0, 0, 0, 0, 0, 0, 1]),
    (1, 1, 0): np.array([1, 0, 0, 0, 0, 0, 0]),
    (1, 0, 1): np.array([0, 1, 0, 0, 0, 0, 0]),
    (0, 1, 1): np.array([0, 0, 1, 0, 0, 0, 0]),
    (1, 1, 1): np.array([0, 0, 0, 1, 0, 0, 0])
}

def error_detect_correct(string: str):
    v = np.array([int(s) for s in string])
    
    parity_check = parity_check_matrix @ v

    tup = (parity_check[0] % 2, parity_check[1] % 2, parity_check[2] % 2)

    return "".join([str(s % 2) for s in (decode_matrix @ error_fix(v, tup))]) 

def error_fix(original, tup: tuple):
    return original + errorMap[tup]

print("Enter a bit string that has a length equal to a multiple of 7:")
input = input()

final = ""

start = 0
while start < len(input):
    cur = input[start: start + 7]

    final += error_detect_correct(cur)

    start += 7

print(f"\nThe decoded bit string is the following:\n{final}")