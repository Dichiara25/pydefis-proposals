def list_creation(number, N):
    i = 0
    values = []
    values.append(number)

    for i in range(N):
        j = 0
        digits = list(str(number))
        number_of_digits = len(digits)
        number = 0

        for j in range(number_of_digits):
            number += round(int(digits[j])**2)
            
        values.append(number)
    
    return values

def compare(values):
    i = 0
    occurence = False
    forbidden_values = [4, 16, 37, 58, 89, 145, 42, 20, 4]

    for i in range(len(values)):
        j = 0
        while(int(values[i + j]) == forbidden_values[j] and j < len(forbidden_values) - 1 and i + j < len(values) - 1):
            j += 1

        if j == len(forbidden_values) - 1:
            occurence = True

    return 1 if occurence == True else 0

def main():
    i = 0
    count = 0
    N = 100

    for i in range(N):
        values = list_creation(i, N)
        count += compare(values)

    print("Occurences : {}".format(count))

if __name__ == "__main__":
    main()