#!/usr/bin/python3

import sys

def generate_password_variations(input_file, output_file):
    with open(input_file, 'r') as file:
        usernames = file.read().splitlines()

    variations = ['password','Password','PASSWORD','admin','Admin','ADMIN']

    for username in usernames:
        name_parts = username.split()

        # If both first and last names are present
        if len(name_parts) == 2:
            first_name, last_name = name_parts
            first_name = first_name.lower()
            last_name = last_name.lower()

            # First and last name variations
            first_variations = [
                first_name, first_name.capitalize(), first_name.upper(),
                first_name + '1', first_name.capitalize() + '1', first_name.upper() + '1',
                first_name + '!', first_name.capitalize() + '!', first_name.upper() + '!',
            ]
            last_variations = [
                last_name, last_name.capitalize(), last_name.upper(),
                last_name + '1', last_name.capitalize() + '1', last_name.upper() + '1',
                last_name + '!', last_name.capitalize() + '!', last_name.upper() + '!',
            ]

            # Combinations of first and last names
            combined_variations = [
                f"{first_name}{last_name}",
                f"{first_name}_{last_name}",
                f"{first_name}.{last_name}",
                f"{first_name}{last_name}1",
                f"{first_name}_{last_name}1",
                f"{first_name}.{last_name}1",
                f"{first_name}{last_name}!",
                f"{first_name}_{last_name}!",
                f"{first_name}.{last_name}!",
                f"{first_name.capitalize()}{last_name.capitalize()}",
                f"{first_name.capitalize()}_{last_name.capitalize()}",
                f"{first_name.capitalize()}.{last_name.capitalize()}",
                f"{first_name.capitalize()}{last_name.capitalize()}1",
                f"{first_name.capitalize()}_{last_name.capitalize()}1",
                f"{first_name.capitalize()}.{last_name.capitalize()}1",
                f"{first_name.capitalize()}{last_name.capitalize()}!",
                f"{first_name.capitalize()}_{last_name.capitalize()}!",
                f"{first_name.capitalize()}.{last_name.capitalize()}!",
                f"{first_name.upper()}{last_name.upper()}",
                f"{first_name.upper()}_{last_name.upper()}",
                f"{first_name.upper()}.{last_name.upper()}",
                f"{first_name.upper()}{last_name.upper()}1",
                f"{first_name.upper()}_{last_name.upper()}1",
                f"{first_name.upper()}.{last_name.upper()}1",
                f"{first_name.upper()}{last_name.upper()}!",
                f"{first_name.upper()}_{last_name.upper()}!",
                f"{first_name.upper()}.{last_name.upper()}!"
            ]

            variations.extend(first_variations + last_variations + combined_variations)

        # If only the first name is present
        elif len(name_parts) == 1:
            first_name = name_parts[0].lower()

            first_variations = [
                first_name, first_name.capitalize(), first_name.upper(),
                first_name + '1', first_name.capitalize() + '1', first_name.upper() + '1',
                first_name + '!', first_name.capitalize() + '!', first_name.upper() + '!'
            ]
            variations.extend(first_variations)

    # Write all variations to the output file
    with open(output_file, 'w') as file:
        for variation in variations:
            file.write(variation + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python user2pass.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = 'user2pass.out'
    generate_password_variations(input_file, output_file)
    print(f"Password variations saved to {output_file}")
