# wc.py

import sys
import argparse

def count_lines(text):
    return len(text.splitlines())

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def wc(text):
    num_lines = count_lines(text)
    num_words = count_words(text)
    num_characters = count_characters(text)
    
    return num_lines, num_words, num_characters

# Main function for command-line usage
def main():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='A Python implementation of the wc utility.')
    
    # Add arguments to the parser
    parser.add_argument('files', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help='File(s) to read from. If omitted or "-", will read from STDIN.')
    parser.add_argument('-l', '--lines', action='store_true', help='Count the number of lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count the number of words')
    parser.add_argument('-c', '--characters', action='store_true', help='Count the number of characters')

    # Now we can parse the arguments
    args = parser.parse_args()

    # Process the files
    total_lines, total_words, total_characters = 0, 0, 0
    for file in args.files:
        text = file.read()
        counts = wc(text)
        total_lines += counts[0]
        total_words += counts[1]
        total_characters += counts[2]
        output = [str(count) for count in counts]
        print(f"{' '.join(output)} {file.name if file.name != '<stdin>' else ''}")
    
    # If more than one file, print the totals
    if len(args.files) > 1:
        print(f"{total_lines} {total_words} {total_characters} total")



if __name__ == '__main__':
    main()
