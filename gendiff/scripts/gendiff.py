#!/usr/bin/env python3
from gendiff.modules import parser
from gendiff.modules.gendiff import generate_diff


def main():
    diff = generate_diff(parser.args.first_file, parser.args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
