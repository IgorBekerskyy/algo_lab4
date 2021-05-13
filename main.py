from collections import defaultdict


def final_number_of_ways (file):
    final_corridor, columns, rows = read_file(file)
    memoized_path_number = defaultdict(int)
    tiles = [[1] for row in range(rows)]
    for row in range(rows):
        memoized_path_number[final_corridor[row][0]] += 1
    for column in range(1, columns):
        successful_ways = {}
        for row in range(rows):
            letter = final_corridor[row][column]
            if letter is not final_corridor[row][column - 1]:
                current_value = tiles[row][column - 1] + memoized_path_number[letter]
            else:
                current_value = memoized_path_number[letter]
            tiles[row].append(current_value)
            successful_ways[letter] = current_value + successful_ways.get(letter, 0)
        for letter in successful_ways:
            memoized_path_number[letter] += successful_ways[letter]
    return finish_corridor(tiles)


def finish_corridor(tiles):
    if len(tiles) > 1:
        return tiles[0][-1] + tiles[-1][-1]
    else:
        return tiles[0][-1]


def read_file(file):
    with open(file, 'r') as input_file:
        data = input_file.readlines()
        columns, rows = [int(number) for number in data[0].split()]
        corridor = [str(line).replace("\n", "") for line in data[1:]]
        final_corridor = [[column for column in corridor[row]] for row in range(rows)]
        return final_corridor, columns, rows


if __name__ == '__main__':
    print(final_number_of_ways("data/ijones3.in"))