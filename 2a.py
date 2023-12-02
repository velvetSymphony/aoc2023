#!/usr/bin/env python3
import sys

base = {'red': 12, 'green': 13, 'blue': 14}

def convert_sentence_dict(specific_set):
    y = dict()
    for num in specific_set.split(', '):
        if 'red' in num:
            y['red'] = int(num.split(" ")[0])
        elif 'blue' in num:
            y['blue'] = int(num.split(" ")[0])
        elif 'green' in num:
            y['green'] = int(num.split(" ")[0])
    return y


def load_lines(file_name):
	with open(file_name, mode='r') as f:
		lines = f.readlines()
		for line in lines:
			yield line


def check_game_id(line):
    game_id, cube_config = line.split(': ')
    uid = game_id.split(' ')[1]
    specific_sets = list()
    specific_sets = cube_config.split('; ')
    new_lines = list()
    for specific_set in specific_sets:
        dict1 = convert_sentence_dict(specific_set)
        new_lines.append(dict1)
    return (uid, new_lines)


def possible_games(game_id, game):
    for combination in game[game_id]:
        if combination.get('red', 0) > base['red'] or combination.get('blue', 0) > base['blue'] or combination.get('green', 0) > base['green']:
            return '0'
    return game_id

if __name__ == '__main__':
    sum_list = list()
    file_name = sys.argv[1]
    lines = load_lines(file_name)
    for line in lines:
        game = dict()
        formatted_line = line.rstrip('\n')
        game_id, combinations = check_game_id(formatted_line)
        game[game_id] = combinations
        games = possible_games(game_id, game)
        print(games)
        sum_list.append(int(games))
    print(sum_list)
    print(sum(sum_list))
