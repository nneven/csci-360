import numpy as np
from collections import deque
from lab1_utils import TextbookStack, apply_sequence
from lab1 import breadth_first_search, depth_first_search


def permutation_number(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    print("2^" + str(n) + " x " + str(n) + "! = " + str(2 ** n) + " x " + str(fact) + " = ")

    n = 2 ** n
    n = n * fact
    print(str(n) + " possible combinations")
    return n


def all_combinations(n):
    order = []
    orientations = []
    for i in range(n):
        order.append(i)
        orientations.append(0)
    stack = TextbookStack(order, orientations)
    total_permutations = permutation_number(n)

    flip_sequence = []
    node = stack.copy(), flip_sequence
    frontier = deque([node])
    reached = [node]

    while frontier:
        node = frontier.popleft()
        n_stack = node[0]
        # if n_stack.check_ordered():
            # return node[1]

        for i in range(1, len(n_stack.order) + 1):
            new_stack = n_stack.copy()
            new_stack.flip_stack(i)
            new_sequence = node[1].copy()
            new_sequence.append(i)
            new_node = new_stack, new_sequence
            if len(reached) == total_permutations:
                return reached
            # print(new_node, reached)
            exists = False
            for j in reached:
                if new_node[0] == j[0]:
                    exists = True
            if not exists:
                frontier.append(new_node)
                reached.append(new_node)


for n in range(1, 6):
    print("For n = " + str(n))
    bfs_total = 0
    bfs_results = []
    dfs_total = 0
    dfs_results = []
    textbook_stacks = all_combinations(n)
    print("All " + str(len(textbook_stacks)) + " combinations found")
    print("Running BFS/DFS on combinations...")
    for stack in textbook_stacks:
        bfs_sequence = breadth_first_search(stack[0])
        dfs_sequence = depth_first_search(stack[0])
        bfs_total += len(bfs_sequence)
        bfs_results.append(len(bfs_sequence))
        dfs_total += len(dfs_sequence)
        dfs_results.append(len(dfs_sequence))

    bfs_average = float(bfs_total) / len(textbook_stacks)
    dfs_average = float(dfs_total) / len(textbook_stacks)

    print("BFS Results: ", end=" ")
    print(bfs_results)
    print("BFS Average: " + str(bfs_average))
    print("DFS Results: ", end=" ")
    print(dfs_results)
    print("DFS Average: " + str(dfs_average))
    print()

