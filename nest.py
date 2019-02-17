#!/usr/bin/python

import argparse
import io
import json
import sys

from util import create_final_dict


parser = argparse.ArgumentParser(
    description="Create nested dict from given json"
)
parser.add_argument('keys', nargs='+', type=str,
                    help="keys for nested dict")


args = parser.parse_args()


def main():
    try:
        input_data = json.loads(
            io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8-sig').read()
        )
        data = create_final_dict(input_data, args.keys)
        print(data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
