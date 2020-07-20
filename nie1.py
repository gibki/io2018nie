S = input()
T = input()

def is_subsequence(pattern, sequence):
    index = 0

    for character in pattern:
        # skip over different characters
        while index < len(sequence) and sequence[index] != character:
            index += 1

        # use found character
        index += 1

    return index <= len(sequence)

def generate_longer_sequences(sequence):
    for split in range(len(sequence)+ 1):
        for character in 'ACGT':
            yield sequence[:split] + character + sequence[split:]


old_sequence = 'enter the loop at least once'
new_sequence = ''

while new_sequence != old_sequence:
    old_sequence = new_sequence

    for sequence in generate_longer_sequences(old_sequence):
        if is_subsequence(sequence, S) and is_subsequence(sequence, T):
            new_sequence = sequence
            break


print(new_sequence)
