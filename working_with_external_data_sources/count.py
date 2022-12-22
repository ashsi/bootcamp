""" Count the number of characters, vowels, words and lines in a file. """

# Instantiate count variables.
char_count, vowel_count, word_count, line_count = 0, 0, 0, 0

# Calculate counts for the file count_input.txt.
with open("count_input.txt", "r") as f:
    for line in f:
        char_count += len(line)
        for char in line:
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowel_count += 1
        word_count += len(line.split())
        line_count += 1

# Print counts.
print(f"Number of characters: {char_count}")
print(f"Number of vowels: {vowel_count}")
print(f"Number of words: {word_count}")
print(f"Number of lines: {line_count}")
