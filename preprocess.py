#!/usr/local/bin/python3
def append_strings_to_lines(input_filename, output_filename, string_list):
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            # Iterate through each line in the input file
            for line in input_file:
                # Remove leading and trailing whitespace from the input line
                line = line.strip()

                # Append each string from the list to the line and write to the output file
                for string in string_list:
                    appended_line = f"{line} {string}\n"
                    output_file.write(appended_line)

        print(f"Done")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Input and output file names
input_file_name = 'phonetic_variations.txt'
output_file_name = 'initials_appended.txt'

# List of strings to append
strings_to_append = ['V P', 'Vijay Prathab', 'Prathab', 'P']

# Call the function to append the list of strings to lines
append_strings_to_lines(input_file_name, output_file_name, strings_to_append)