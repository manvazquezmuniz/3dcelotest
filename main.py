import sys
import Part1
import Part2


def main(*args):
    """ Class for execution of main task """
    # Get input from file
    input_file = open("input.txt")
    puzzle_input = input_file.read()
    input_file.close()

    # Transform input into list of lists of integers
    trees = [[int(tree) for tree in line] for line in puzzle_input.splitlines()]

    # Execute desired test case
    if not args or args[0] == "Part1":
        Part1.execute(trees)
    if not args or args[0] == "Part2":
        Part2.execute(trees)


if __name__ == '__main__':
    # Execute main task. Possible arguments: Part1 for first part, Part2 for second part, Nothing for executing both
    main(*sys.argv[1:])
