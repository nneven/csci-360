# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque
from lab1_utils import TextbookStack, apply_sequence


def breadth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    node = stack.copy(), flip_sequence
    frontier = deque([node])
    reached = [node]

    while frontier:
        node = frontier.popleft()
        n_stack = node[0]
        # print(n_stack)
        if n_stack.check_ordered():
            return node[1]

        for i in range(1, len(n_stack.order) + 1):
            new_stack = n_stack.copy()
            new_stack.flip_stack(i)
            new_sequence = node[1].copy()
            new_sequence.append(i)
            new_node = new_stack, new_sequence
            if new_stack.check_ordered():
                # print(new_sequence)
                return new_sequence
            # print(new_node, reached)
            exists = False
            for j in reached:
                if new_node[0] == j[0]:
                    exists = True
            if not exists:
                frontier.append(new_node)
                reached.append(new_node)

    # ---------------------------- #


def depth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    node = stack.copy(), flip_sequence
    frontier = deque([node])
    reached = [node]

    while frontier:
        node = frontier.pop()
        n_stack = node[0]
        if n_stack.check_ordered():
            return node[1]

        for i in range(1, len(n_stack.order) + 1):
            new_stack = n_stack.copy()
            new_stack.flip_stack(i)
            new_sequence = node[1].copy()
            new_sequence.append(i)
            new_node = new_stack, new_sequence
            if new_stack.check_ordered():
                # print(new_sequence)
                return new_sequence
            exists = False
            for j in reached:
                if new_node[0] == j[0]:
                    exists = True
            if not exists:
                frontier.append(new_node)
                reached.append(new_node)

    # ---------------------------- #

