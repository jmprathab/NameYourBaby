#!/usr/local/bin/python3
def calculate_numerology(name):
    # Define a dictionary to map letters to their numerology values
    numerology_values = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 8, 'g': 3, 'h': 5, 'i': 1,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 7, 'p': 8, 'q': 1, 'r': 2,
        's': 3, 't': 4, 'u': 6, 'v': 6, 'w': 6, 'x': 5, 'y': 1, 'z': 7
    }

    name = name.lower()
    numerology_value = sum(numerology_values.get(letter, 0) for letter in name)

    while numerology_value > 9:
        numerology_value = sum(int(digit) for digit in str(numerology_value))

    return numerology_value

# Read names from input file and calculate numerology values
with open("initials_appended.txt", "r") as input_file:
    names = input_file.readlines()

name_values = [(name.strip(), calculate_numerology(name.strip())) for name in names]

# Sort the name-value pairs by the numerology value, with 6 coming first
name_values.sort(key=lambda x: (x[1] != 6, x[1]))

# Write the sorted results to an output file
with open("names.txt", "w") as output_file:
    for name, value in name_values:
        output_file.write(f"{name}, {value}\n")

print("Done")