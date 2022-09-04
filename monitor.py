import os
import time
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, required=True)
parser.add_argument('-d', '--dir', type=str, required=True)
parser.add_argument('-q', '--query', type=str)
parser.add_argument('-m', '--monitor', type=bool)
parser.add_argument('-r', '--read', type=bool)
parser.add_argument('-s', '--size', type=int)
args = parser.parse_args()


def follow(path):
    with open(path, "r") as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line


def get_file_path(name, dir):
    return os.path.join(dir, f'{name}.log')


def read_in_chunks(file, chunk_size):
    data = []
    counter = 0
    for n, line in enumerate(file, start=1):
        counter += 1
        data.append(line)
        if not n % chunk_size:
            yield data, counter
            data = []
    if data:
        yield data, counter


def log_entry_query(line, query):
    if query in line:
        return line


def search_query(filepath, query):
    current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    with open(filepath) as file:
        for piece in read_in_chunks(file,  args.size):
            if query:
                lines = []
                with open(get_file_path(f'{current_time}_{query}',  './'), 'a+') as new_file:
                    for line in filter(lambda x: log_entry_query(x, query), file):
                        new_file.write(line)


def main():

    filepath = get_file_path(args.file, args.dir)
    if args.query:
        search_query(filepath, args.query)
    if args.monitor:
        loglines = follow(filepath)
        for line in loglines:
            print(line)
    if args.read:
        with open(filepath) as file:
            for chunk in read_in_chunks(file, args.size):
                data, counter = chunk
                print(f'chunk part {counter}:')
                print(f'{data}')
                print('\n')


if __name__ == '__main__':
    main()
