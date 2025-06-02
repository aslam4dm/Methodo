#!/usr/bin/env python

import argparse
import requests
import yaml  # You'll need to install pyyaml: pip install pyyaml
import pyfiglet
from colorama import Fore, Style

def check_gtfobins(binary_name):
    url = f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{binary_name}.md"
    response = requests.get(url)
    
    if response.status_code == 200:
        yaml_front_matter = response.text.split('---')[1]  # Get YAML front matter
        data = yaml.safe_load(yaml_front_matter)  # Load YAML data
    else: return
         
    print(f"{Fore.MAGENTA}{pyfiglet.figlet_format(binary_name, font='slant',justify='left')}{Style.RESET_ALL}")
    
    sections = data["functions"]
    for s in sections:
        category = sections[s]
        for c in category:
            print("Type:\t" + f"{Fore.RED}{s}{Style.RESET_ALL}")
            if "description" in c:
                print("Desc:\t" + f"{Fore.GREEN}{(c['description'])}{Style.RESET_ALL}")
            print("Code:\t" + f"{Fore.WHITE}" + c['code'].replace("\n", "\n\t") + f"{Style.RESET_ALL}")
            print("\n")

def main():
    parser = argparse.ArgumentParser(description='GTFOBins Checker')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--binary-name', '-bn', help='Name of the binary to search')
    group.add_argument('--binary-file', '-bf', help='File containing names of binaries')
    args = parser.parse_args()

    if args.binary_name:
        check_gtfobins(args.binary_name)
    elif args.binary_file:
        with open(args.binary_file, 'r') as file:
            for line in file:
                check_gtfobins(line.strip())

if __name__ == "__main__":
    main()
