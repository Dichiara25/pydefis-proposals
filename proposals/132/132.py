from math import sqrt

def decompose_number(number):
    number = str(number)
    decomposed_number = []

    for i in range(len(number)):
        decomposed_number.append(number[i])

    return decomposed_number

def is_sequence_valid(number):
    valid_number_sequence = [1, 2, 4, 6, 7]
    invalid_number_sequence = [3, 5, 8, 9, 0]

    for i in range(len(number)):
        if int(number[i]) in valid_number_sequence:
            valid_number_sequence.remove(int(number[i]))
        elif int(number[i]) in invalid_number_sequence:
            return False

    if len(valid_number_sequence) == 0:
        return True
    else:
        return False

def reassemble_number(number):
    reassembled_number = ""
    
    for i in range(len(number)):
        reassembled_number = reassembled_number + number[i]

    return int(reassembled_number)

def main():
    next_combinations = []
    n = 64225

    while len(next_combinations) < 3:
        decomposed_number = decompose_number(pow(n,2))
        if is_sequence_valid(decomposed_number):
            number = reassemble_number(decomposed_number)
            next_combinations.append(round(sqrt(number)))
        n += 1

    print(next_combinations)

if __name__ == "__main__":
    main()