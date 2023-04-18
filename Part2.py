from typing import List


def visible_trees(size: int, tree_line: List[int]) -> int:
    """ Function for checking the number of trees visible from a given tree in a given line or direction

    Args:
        size: Height of the given tree
        tree_line: List of subsequent tree heights, starting from closer to given tree
    """
    # Vision length from current tree
    view_length = 0

    # Iterate over subsequent trees
    for tree in tree_line:
        # Increase vision length
        view_length += 1
        if tree >= size:
            # If current tree is taller or equal height to reference tree, return the current vision length
            return view_length

    # If all trees are smaller in the line (or there are no trees), return the length of the given tree line
    return view_length


def execute(trees: List[List[int]]):
    """ Function for executing second part of test

    Args:
        trees: List of lists of integers specifying tree height
    """
    # Variable declaring the maximum amount of trees visible from any tree
    scenic_score = 0

    # Iterate over all trees, saving the position
    for row_idx, line in enumerate(trees):
        for col_idx, tree in enumerate(line):
            # Get number of trees visible in every direction
            left_view = visible_trees(tree, line[col_idx - 1::-1])
            right_view = visible_trees(tree, line[col_idx + 1:])
            top_view = visible_trees(tree, [tree_l[col_idx] for tree_l in trees][row_idx - 1::-1])
            bottom_view = visible_trees(tree, [tree_l[col_idx] for tree_l in trees][row_idx + 1:])

            # Update maximum scenic score
            scenic_score = max(scenic_score, left_view * right_view * top_view * bottom_view)

    # Print the maximum scenic score (solution)
    print(scenic_score)
