import csv

def read_csv(path):
    data={}
    
    with open(path) as fin:
        reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]]=row[1:]
    
    return data

def decompose(message):
    decomposed_message = []

    i = 0
    while i < len(message):
        if message[i] == "H" and message[i + 1] == "S":
            decomposed_message.append(message[i] + message[i + 1])
            i += 2
        else:
            decomposed_message.append(message[i] + message[i + 1] + message[i + 2])
            i += 3

    return decomposed_message

def reassemble(message):
    reassembled_message = ""
    
    for i in range(len(message)):
        reassembled_message += message[i]

    return reassembled_message


def translate(message):
    alphabet = read_csv('./alphabet.csv')
    decomposed_message = decompose(message)
    translated_message = []

    for i in range(len(decomposed_message)):
        translated_message.append(str(alphabet[decomposed_message[i]][0]))

    translated_message = reassemble(translated_message)
    return translated_message

def main():
    with open("cypher.txt", "r") as f:
        cypher = f.readlines()
    
    message = translate(cypher[0])

    print(message)

if __name__ == "__main__":
    main()
