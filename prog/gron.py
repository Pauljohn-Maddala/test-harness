#!/usr/bin/env python3
# gron.py

import json
import argparse
import sys

def flatten_json(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from flatten_json(v, f"{path}{k}.")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from flatten_json(v, f"{path}{i}.")
    else:
        path = path.rstrip('.')
        value = json.dumps(obj)
        yield f"{path} = {value}"

def gron(json_text):
    json_obj = json.loads(json_text)
    return "\n".join(flatten_json(json_obj))

def main():
    parser = argparse.ArgumentParser(description='Flatten JSON for easy grepping.')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='A filename containing JSON or - for STDIN.')

    args = parser.parse_args()

    try:
        json_input = args.file.read()
        print(gron(json_input))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
