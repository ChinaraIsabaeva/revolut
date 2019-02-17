#!/usr/bin/python

import argparse
import dpath
import io
import json
import sys

parser = argparse.ArgumentParser(
    description="Create nested dict from given json"
)
parser.add_argument('keys', nargs='+', type=str,
                    help="keys for nested dict")


args = parser.parse_args()


def create_list_of_nested_dict(input_data):
    leaf_name = args.keys
    result = []
    for item in input_data:
        unused_keys = list(set(item.keys()) - set(leaf_name))
        item_nested_dict = []
        for key in unused_keys:
            item_nested_dict.append({key: item.get(key)})
        for name in reversed(leaf_name):
            key = item.get(name)
            item_nested_dict = {key: item_nested_dict}
        result.append(item_nested_dict)

    return result


def merge_dict_with_duplicated_keys(input_list):
    final_dict = {}
    for item in input_list:
        for key, value in item.items():
            if key in final_dict:
                final_dict_item = {key: final_dict.get(key)}
                dpath.util.merge(final_dict_item, item)
                final_dict.update(final_dict_item)
            else:
                final_dict.update(item)
    return final_dict


def create_final_dict(input_data):
    input_list = create_list_of_nested_dict(input_data)
    final_dict = merge_dict_with_duplicated_keys(input_list)
    return final_dict


def main():
    try:
        input_data = json.loads(
            io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8-sig').read()
        )
        data = create_final_dict(input_data)
        print(data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
