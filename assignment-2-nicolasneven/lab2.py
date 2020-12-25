# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop


def heuristic(stack):

    h = 0
    for i in range(len(stack.order)-1):
        if stack.order[i] > stack.order[i+1]:
            h += 1
        elif (stack.orientations[i] == 0) and (stack.orientations[i+1] == 0):
            h += 1
        elif stack.order[i] != (stack.order[i+1] - 1) and stack.order[i] != (stack.order[i+1] + 1):
            h += 1
        elif (stack.orientations[i] == 0 and stack.orientations[i+1] == 1) or (stack.orientations[i] == 1 and stack.orientations[i+1] == 0):
            h += 1
    return h


def a_star_search(stack):

    count = 0
    frontier = []
    flip_sequence = []

    start = (stack.copy(), flip_sequence, 0, heuristic(stack))
    heappush(frontier, (start[2] + start[3], start[2], start[3], count, start))

    while frontier:
        node = heappop(frontier)
        parent = node[4]
        parent_stack = parent[0]
        # print(n_stack)
        if parent_stack.check_ordered():
            return parent[1]

        # explore all children
        for i in range(1, len(parent_stack.order) + 1):
            count += 1
            child_stack = parent_stack.copy()
            child_stack.flip_stack(i)
            child_sequence = parent[1].copy()
            child_sequence.append(i)
            child = (child_stack, child_sequence, parent[2] + 1, heuristic(child_stack))
            # print(child[2], child[3])
            heappush(frontier, (child[2] + child[3], child[2], child[3], count, child))


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
