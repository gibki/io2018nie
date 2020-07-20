S = input()
T = input()

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

def count_character(pattern, sequence):
    count = 0

    for character in sequence:
        if character == pattern:
            count += 1

    return count

class SequenceSlider:
    def __init__(self, counted_character, pattern, sequence):
        self._counted_character = character
        self._sequence = sequence
        self._last_occurence_positions = find_positions_of_last_occurence(pattern, sequence) + [len(sequence)]
        self._count = count_character(counted_character, sequence[:self._last_occurence_positions[0]])
        self._left_last_index = 0
        self._right_last_index = 0

    @property
    def count(self):
        return self._count

    def slide(self, added_chunk):
        self._slide_left(added_chunk)
        self._slide_right()

    def _slide_left(self, added_chunk):
        for character in added_chunk:
            while  self._sequence[self._left_last_index] != character:
                if self._sequence[self._left_last_index] == self._counted_character:
                    self._count -= 1
                self._left_last_index += 1

            if self._sequence[self._left_last_index] == self._counted_character:
                self._count -= 1
            self._left_last_index += 1

    def _slide_right(self):
        slide_chunk_start = self._last_occurence_positions[self._right_last_index]
        slide_chunk_end = self._last_occurence_positions[self._right_last_index + 1]
        for character in self._sequence[slide_chunk_start:slide_chunk_end]:
            if character == self._counted_character:
                self._count += 1
        self._right_last_index += 1


longest_common_sequence = ''

for character in ALPHABET:
    s_slider = SequenceSlider(character, longest_common_sequence, S)
    t_slider = SequenceSlider(character, longest_common_sequence, T)

    new_longest_common_sequence = ''

    for common_sequence_character in longest_common_sequence:
        added_chunk = min(s_slider.count, t_slider.count) * character + common_sequence_character

        s_slider.slide(added_chunk)
        t_slider.slide(added_chunk)

        new_longest_common_sequence += added_chunk

    new_longest_common_sequence += min(s_slider.count, t_slider.count) * character
    longest_common_sequence = new_longest_common_sequence


print(longest_common_sequence)
