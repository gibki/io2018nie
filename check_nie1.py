S = input()
T = input()
W = input()

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


if not is_subsequence(W, S):
    print('{} not a subsequence of {}'.format(W, S))
    exit(1)

if not is_subsequence(W, T):
    print('{} not a subsequence of {}'.format(W, T))
    exit(1)

for sequence in generate_longer_sequences(W):
    if is_subsequence(sequence, S) and is_subsequence(sequence, T):
        print('Longer subsequence found: {}'.format(sequence))
        exit(1)
