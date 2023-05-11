import re
import time
import argparse

def replace_string_literals(input_file, output_file='', debug=False):
    if not output_file:
      output_file = input_file + '.o'
    with open(input_file, 'r') as f:
        input_str = f.read()

    original_len = len(input_str)

    if debug:
        print(input_str)


    pattern = r'''(['"])((?:(?<=\\)\1|(?!\1).)*?)\1\s*\+\s*(['"])((?:(?<=\\)\3|(?!\3).)*?)\3'''
    regex = re.compile(pattern)

    while True:
        matches = regex.search(input_str)
        if matches is None:
            break

        replaced_str = regex.sub(lambda m: '"' + m.group(2) + m.group(4) + '"', input_str)
        input_str = replaced_str
        if debug:
            print(input_str)
    
    if not debug:
        print(input_str)
    if debug:
        end_time = time.time()
        print("Elapsed time:", end_time - start_time)
        print("Original string length:", original_len)
        print("Final string length:", len(input_str))

    with open(output_file, 'w') as f:
        f.write(input_str)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replace concatenated string literals in a file')
    parser.add_argument('input_file', help='Input file name')
    parser.add_argument('-o', '--output_file', default='', help='Output file name (default: input_file.o)')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output')
    args = parser.parse_args()

    start_time = time.time()

    replace_string_literals(args.input_file, args.output_file, args.debug)

    if not args.debug:
        end_time = time.time()

        print("Elapsed time:", end_time - start_time)
