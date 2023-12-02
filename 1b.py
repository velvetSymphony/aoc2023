#!/usr/bin/env python3
import sys

numbers = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
}
numbers_rev = {
	'eno': '1',
	'owt': '2',
	'eerht': '3',
	'ruof': '4',
	'evif': '5',
	'xis': '6',
	'neves': '7',
	'thgie': '8',
	'enin': '9',
}


def load_lines(file_name):
	with open(file_name, mode='r') as f:
		lines = f.readlines()
		for line in lines:
			yield line


def reformated_line(line):
	if line[0].isnumeric() and line[len(line) - 1].isnumeric():
		return int(line[0] + line[len(line) - 1])

	elif not (line[0].isnumeric() and line[len(line) - 1].isnumeric()):
		first_num = check_something(line, numbers)
		last_num = check_something(line[::-1], numbers_rev)
		if first_num and last_num:
			return int(first_num + last_num)

	elif line[0].isnumeric():
		new_line = line[1::]
		last_num = check_something(new_line[::-1], numbers_rev)
		return int(last_num + line[0])

	elif line[len(line) - 1].isnumeric():
		first_num = check_something(line[: len(line) - 1], numbers)
		return int(first_num + line[len(line) - 1])


def check_something(line, numbers):
	new_string = ''
	for char in line:
		new_string = new_string + char
		y = check_number(new_string, numbers)
		if y[len(y) - 1].isnumeric():
			return y[len(y) - 1]


def check_number(new_string, numbers):
	number_keys = set(numbers.keys())
	match = [number for number in number_keys if number in new_string]
	if match:
		return new_string.replace(match[0], numbers[match[0]])
	else:
		return new_string


if __name__ == '__main__':
	sum_list = list()
	file_name = sys.argv[1]
	lines = load_lines(file_name)
	for line in lines:
		formatted_line = line.rstrip('\n')
		correct_line = reformated_line(formatted_line)
		sum_list.append(correct_line)
	print(sum(sum_list))
