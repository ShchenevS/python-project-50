#!/usr/bin/env python3
from gendiff.modules import cli
from gendiff.modules.gendiff import generate_diff


def main():
    diff = generate_diff(
        cli.args.first_file,
        cli.args.second_file,
        cli.args.FORMAT)
    print(diff)


if __name__ == '__main__':
    main()
