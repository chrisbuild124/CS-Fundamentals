# @chrisbuild124
# These are some Python built in data Structures and notes.
# This includes: Lists. 
# --------------------------------------Description--------------------------------------

import collections

def main():
    """
    Description: This is the main function for the program.
    """
    lists()
    
def lists():
    """
    Description: This function walks through each function of a list.
    params: Void.
    :returns: Void.
    """

    # Create a list
    # NOTE: Lists are already stacks and LIFO, queues are deque and FIFO
    # List is immutable, so values can be modified as needed. 
    # --------------------------------------Create--------------------------------------
    # Way 1
    example_1 = [
        1,
        2,
        3
    ]
    # Way 2
    example_1 = []  # Dunamic Array
    # Way 3
    # Make a dequeue data structure (Queues)
    example_1 = collections.deque([1, 2, 3])  # Doubly linked list 
    example_1.append(4)  # Data is being modified
    example_1.appendleft(0)  # Data is being modified to the left
    example_1.pop()  # Data is removed from the right
    example_1.popleft()  # Data is removed from the left (O(1)) runttime
    # Way 4
    example_1 = list()
    # Way 5
    example_1 = [1, 2, 3]

    # -----------------------------------Append/Update----------------------------------
    # Way 1: Adds a value to the right
    example_1.append(4)
    # Way 2: Adds a value at a certain index
    example_1.insert(1, 1.5)
    # Way 3: Combines two lists (at end)
    example_1.extend([5, 6])
    # Way 3: Combines two lists (at end)
    example_1 = example_1 + [7]
    
    # -----------------------------------Remove----------------------------------------
    # Way 1: Remove value by index O(n) runttime
    del example_1[4]
    # Way 2: Removes fropm index 2 O(n) runttime
    example_1.pop(2)
    # Way 3: Clear all
    example_1.clear()

    # ------------------------------------Read-----------------------------------------
    # Way 1: Common way to get an value using slicing
    example_1 = [1, 2, 3, 4, 5]
    value = example_1[2]
    # Way 2: Get last index
    value = example_1[-1]
    # Way 3: Get by slicing multiple
    values = example_1[::-1]  # (reverse)
    values = example_1[1:3]

    # ---------------------------------Operations--------------------------------------
    # Operation 1: Convert Python set to a list
    example_1 = {1, 2, 3, 4, 5}
    example_1 = list(example_1)
    # Operation 2: List comprehension
    new_list = [item for item in example_1 if item != 2] # Filters 2
    # Operation 3: sort a list based on values
    new_list.sort()  # O(nlogn) runttime
    # Operation 4: Reverse a list
    new_list.reverse()


if __name__ == '__main__':
    main()
