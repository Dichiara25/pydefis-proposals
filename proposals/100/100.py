def decompose(amount):
    decomposed_amount = []
    amount = str(amount)

    for i in range(len(amount)):
        decomposed_amount.append(amount[i])

    return decomposed_amount

def to_mornille(gallions):
    conversion_ratio = 17
    return gallions * conversion_ratio 

def to_noise(mornilles):
    conversion_ratio = 29
    return mornilles * conversion_ratio 

def is_sequence_valid(gallions):
    mornilles = to_mornille(gallions)
    noises = to_noise(mornilles)

    valid_gallion_sequence = decompose(gallions)
    valid_mornille_sequence = decompose(mornilles)
    valid_noise_sequence = decompose(noises)

    j = 0
    while j < len(decompose(gallions)):
        if decompose(gallions)[j] not in valid_mornille_sequence or decompose(gallions)[j] not in valid_noise_sequence:
            return False
        j += 1

    j = 0
    while j < len(decompose(mornilles)):
        if decompose(mornilles)[j] not in valid_gallion_sequence or decompose(mornilles)[j] not in valid_noise_sequence:
            return False
        j += 1

    j = 0
    while j < len(decompose(noises)):
        if decompose(noises)[j] not in valid_gallion_sequence or decompose(noises)[j] not in valid_mornille_sequence:
            return False
        j += 1
    
    return True

def main():
    n = 1000000
    i = 1

    while not is_sequence_valid(i):
        i += 1

    print(i)

if __name__ == "__main__":
    main()