#!/usr/bin/env python3
import sys


def load_lines(file_name):
	with open(file_name, mode='r') as f:
		lines = f.readlines()
		for line in lines:
			yield line


def check_numeric(line):
	num_char = [char for char in line if char.isnumeric()]
	return num_char[0]


if __name__ == '__main__':
    sum_list = list()
    file_name = sys.argv[1]
    lines = load_lines(file_name)
    for line in lines:
        formatted_line = line.rstrip('\n')
        num = check_numeric(formatted_line) + check_numeric(formatted_line[::-1])
        sum_list.append(int(num))
    print(sum(sum_list))
