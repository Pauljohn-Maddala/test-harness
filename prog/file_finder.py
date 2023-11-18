# file_finder.py

import os
import fnmatch
import argparse
from datetime import datetime

def file_finder(root_dir, pattern='*', min_size=None, max_size=None, before=None, after=None, recursive=True):
    matches = []
    for path, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, pattern):
            full_path = os.path.join(path, filename)
            stats = os.stat(full_path)
            file_size = stats.st_size
            file_mtime = datetime.fromtimestamp(stats.st_mtime)
            if min_size and file_size < min_size:
                continue
            if max_size and file_size > max_size:
                continue
            if before and file_mtime > before:
                continue
            if after and file_mtime < after:
                continue
            matches.append(full_path)
        if not recursive:
            break
    return matches

def main():
    parser = argparse.ArgumentParser(description='Search for files based on various criteria.')
    parser.add_argument('./test/', help='Root directory to search for files.')
    # Add other parser arguments as needed
    args = parser.parse_args()
    matches = file_finder(args.root_dir) # and other arguments
    for match in matches:
        print(match)

if __name__ == '__main__':
    main()

