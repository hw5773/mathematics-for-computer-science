import re
import sys
import argparse
import logging
import os

def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set

def run(fname):
    with open(fname, "r") as f:
        for line in f:
            print ("{}: {}".format(line, extract_variables(line)))

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", metavar="<input file that contains propositions>", help="Input file that contains propositions", type=str, required=True)
    parser.add_argument("-l", "--log", metavar="<log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)>", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not os.path.exists(args.input):
        logging.error("File not exist: {}".format(args.input))
        sys.exit(1)

    run(args.input)

if __name__ == "__main__":
    main()
