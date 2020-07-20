S = input()
T = input()
W = input()


ALPHABET = 'ACGT'


def find_positions_of_first_occurence(pattern, sequence):
    positions = []
    index = 0

    for character in pattern:
        # skip over different characters
        while index < len(sequence) and sequence[index] != character:
            index += 1

        # use found character
        if index < len(sequence):
            positions.append(index)
            index += 1
        else:
            return []

    return positions

def find_positions_of_last_occurence(pattern, sequence):
    return [len(sequence) - 1 - x for x in
        reversed(find_positions_of_first_occurence(reversed(pattern), list(reversed(sequence))))]

def calculate_chunk_counts(character, pattern, sequence):
    first_occurence_positions = find_positions_of_first_occurence(pattern, sequence)
    last_occurence_positions = find_positions_of_last_occurence(pattern, sequence)

    # adjust for range inclusion, add terminators
    first_occurence_positions = [0] + [x + 1 for x in first_occurence_positions]
    last_occurence_positions = last_occurence_positions + [len(sequence)]

    counts = []
    current_count = 0

    for c in sequence[:last_occurence_positions[0]]:
        if c == character:
            current_count += 1
    counts.append(current_count)

    for pattern_index in range(len(pattern)):
        for sequence_index in range(first_occurence_positions[pattern_index],
                                    first_occurence_positions[pattern_index + 1]):
            if sequence[sequence_index] == character:
                current_count -= 1

        for sequence_index in range(last_occurence_positions[pattern_index],
                                    last_occurence_positions[pattern_index + 1]):
            if sequence[sequence_index] == character:
                current_count += 1

        counts.append(current_count)

    return counts


if not find_positions_of_first_occurence(W, S):
    print('{} not a subsequence of {}'.format(W, S))
    exit(1)

if not find_positions_of_first_occurence(W, T):
    print('{} not a subsequence of {}'.format(W, T))
    exit(1)

for character in ALPHABET:
    for split, (count_S, count_T) in enumerate(zip(calculate_chunk_counts(character, W, S),
                                                   calculate_chunk_counts(character, W, T))):
        if count_S * count_T > 0:
            print('Longer subsequence found: {}{}{}'.format(W[:split], character, W[split:]))
            exit(1)
