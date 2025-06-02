#!/usr/bin/python3

import itertools
import sys

def generate_usernames(first_name, last_name=None):
    first_initial = first_name[0]
    
    combinations = [
        f"{first_name}",
        f"{first_initial}",
    ]
    
    if last_name:
        last_initial = last_name[0]
        
        combinations.extend([
            f"{first_name}.{last_initial}",
            f"{first_name}{last_initial}",
            f"{first_name}_{last_initial}",
            f"{last_initial}.{first_name}",
            f"{last_initial}{first_name}",
            f"{last_initial}_{first_name}",
            f"{first_initial}.{last_name}",
            f"{first_initial}{last_name}",
            f"{first_initial}_{last_name}",
            f"{first_name}.{last_name}",
            f"{first_name}{last_name}",
            f"{first_name}_{last_name}",
            f"{last_name}.{first_name}",
            f"{last_name}{first_name}",
            f"{last_name}_{first_name}"
        ])
    
    return combinations

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        names = [line.strip() for line in file.readlines()]
    return names

def write_output_file(output_path, username_list):
    with open(output_path, 'w') as file:
        for username in username_list:
            if len(username) > 1:
                file.write(f"{username}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python name2username.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = 'full_usernames.txt'  # Path to your output file
    
    # Read names from input file
    names = read_input_file(input_file)
    
    # Generate usernames for each name
    all_usernames = []
    for name in names:
        name_parts = name.split()
        
        if len(name_parts) == 2:  # First Last
            first_name, last_name = name_parts
            usernames = generate_usernames(first_name.lower(), last_name.lower())
        elif len(name_parts) == 1:  # Just First or First.Last
            if '.' in name_parts[0]:  # First.Last
                first_name, last_name = name_parts[0].split('.')
                usernames = generate_usernames(first_name.lower(), last_name.lower())
            else:  # Just First
                first_name = name_parts[0]
                usernames = generate_usernames(first_name.lower())
        else:
            continue  # Skip invalid entries

        all_usernames.extend(usernames)
    
    # Write usernames to output file
    write_output_file(output_file, all_usernames)

    print("Usernames generated successfully.")
