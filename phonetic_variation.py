#!/usr/local/bin/python3
import re

# Define a list of common phonetic substitutions
phonetic_substitutions = [
    ('a', 'aa'),
    ('aa', 'a'),
    ('ee', 'i'),
    ('s', 'sh'),
    ('sh', 's'),
    ('k', 'kh'),
    ('kh', 'k'),
    ('g', 'gh'),
    ('gh', 'g'),
    ('c', 'ch'),
    ('ch', 'c'),
    ('j', 'jh'),
    ('jh', 'j'),
    ('t', 'th'),
    ('th', 't'),
    ('th', 'dh'),
    ('dh', 'th'),
    ('d', 'dh'),
    ('dh', 'd'),
    ('p', 'ph'),
    ('ph', 'p'),
    ('b', 'bh'),
    ('bh', 'b'),
    ('v', 'w'),
    ('w', 'v'),
    ('ga', 'ha'),
    ('ba', 'bha'),
    ('tu', 'thu'),
]

def generate_similar_sounding_names(name):
    similar_names = set()
    similar_names.add(name)

    # Apply phonetic substitutions
    for substitution in phonetic_substitutions:
        pattern, replace = substitution
        new_name = re.sub(pattern, replace, name)
        similar_names.add(new_name)

    return list(similar_names)

# Function to apply to each word in a line
def process_word(word):
    # Modify this function to produce multiple outputs for each word
    return generate_similar_sounding_names(word)

# Input and output file names
input_filename = 'raw.names'
output_filename = 'phonetic_variations.txt'

try:
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        # Iterate through each line in the input file
        for line in input_file:
            # Remove leading and trailing whitespace from the line
            line = line.strip()

            # Split the line into words
            words = line.split()

            # Process each word and write the results to the output file
            for word in words:
                outputs = process_word(word)
                for output in outputs:
                    output_file.write(output + '\n')

    print(f"Done")
except FileNotFoundError:
    print("File not found. Please check the file path.")
