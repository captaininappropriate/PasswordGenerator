#! python
########################################################################
# Author : Greg Nimmo
# Version : 0.1
# Description : A very simple password generator.
#######################################################################


import argparse
import random
import string
import sys

def main() -> None:
    # argparse command-line arguments
    parser = argparse.ArgumentParser(description="A simple password generator", prog=sys.argv[0])
    parser.add_argument("-n", "--number", default=8, metavar="N", help="N number of characters to generate", type=int)
    parser.add_argument("-u", "--uppercase", default=True, action="store_true", help="Include uppercase letters")
    parser.add_argument("-l", "--lowercase", default=True, action="store_true", help="Include lowercase letters")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-v", "--version", action="version", version=sys.argv[0] + " v1.0")

    arguments = parser.parse_args()

    character_combination: list = []

    # add the required characters to the lisst for randomly sampling
    if arguments.uppercase == True:
        character_combination.extend(list(string.ascii_uppercase))
    if arguments.lowercase == True:
        character_combination.extend(list(string.ascii_lowercase))
    if arguments.special == True:
        character_combination.extend(list(string.punctuation))
    if arguments.digits == True:
        character_combination.extend(list(string.digits))

    # randomly sample the character list and print the resulting password based on the length requirement
    print("".join(random.sample(character_combination, arguments.number)))


if __name__ == "__main__":
    main()

