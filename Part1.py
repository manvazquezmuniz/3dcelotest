from typing import List


def execute(trees: List[List[int]]):
    """ Function for executing first part of test

    Args:
        trees: List of lists of integers specifying tree height
    """
    # Variable declaring the trees that are visible
    visible_trees = set()

    # Iterate over all trees, saving the position
    for row_idx, line in enumerate(trees):
        for col_idx, tree in enumerate(line):
            # Check if tree is in first or last row or column, or if it's taller than previous or later trees in the
            # same row or column
            if col_idx in [0, len(line) - 1] or row_idx in [0, len(trees) - 1] or\
                    tree > max(line[:col_idx]) or tree > max(line[col_idx + 1:]) or\
                    tree > max([tree_l[col_idx] for tree_l in trees[:row_idx]]) or\
                    tree > max([tree_l[col_idx] for tree_l in trees[row_idx + 1:]]):
                # If tree is visible, add it to list of visible trees
                visible_trees.add((row_idx, col_idx))

    # Print the amount of visible trees (solution)
    print(len(visible_trees))
