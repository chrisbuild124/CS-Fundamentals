# @chrisbuild124
# These are Python built in data Structures and notes.
# This includes: Dictionary, Sets, Lists, and Tuples
# --------------------------------------Description--------------------------------------

import collections


def main():
    """
    Description: This is the main function for the program.
    """
    dictionaries()
    lists()


def dictionaries():
    """
    Description: This function walks through each function of a dictionary.
    params: Void.
    :returns: Void.
    """

    # Create a dictionary
    # Keys must be immutable typesa, values are mutable
    # --------------------------------------Create--------------------------------------
    # Way 1
    example_1 = {
        1: '1',
        2: 'b',
        3: 'c'
    } 
    # Way 2
    example_1 = {}
    # Way 3
    # Default value is 0 for integers, can modify data with 0 as default
    example_1 = collections.defaultdict(int)
    example_1[1] += 1  # Data is being modified
    example_1 = collections.defaultdict(list)
    # Should add the following without already adding a list: {1: [2]}
    example_1[1].append(2)
    # Way 4
    example_1 = dict()
    # Way 5
    example_1[1] = 'a'
    example_1[2] = 'b'
    example_1[3] = 'c'
    # Way 6
    example_1 = {1: 'a', 2: 'b', 3: 'c'}

    # -----------------------------------Append/Update----------------------------------
    # Way 1: This will create if not in dictionary, otherwise it will update it
    example_1[4] = 'd'
    # Way 2: If 4 does not exist in the dictionary, adds 4:x, otherwise nothing
    value = example_1.setdefault(4, 'x')
    # Way 3: Updates if there, if not creates in dict
    example_1.update({"color": "White"})  
    
    # -----------------------------------Remove----------------------------------------
    # Way 1: Remove value by key
    del example_1[4]
    # Way 2: Removes 4 from dictionary, returns None if not there
    ShouldBeNone = example_1.pop(4, None)
    # Way 3: Clear all
    example_1.clear()

    # ------------------------------------Read-----------------------------------------
    # Way 1: Common way to get an value, could raise KeyError
    example_1[1] = 'a'
    read_a = example_1[1]
    # Way 2: Another way to get a value, will not raise KeyError
    read_a_default = example_1.get(1, 'None')  # Default is None

    # ---------------------------------Operations--------------------------------------
    # Operation 1: Convert Python dictionary to a dict_items class
    dict_items = example_1.items()
    # Operation 2: Convert Python dict_items class to list, key: value
    new_list = list(dict_items)
    # Combine Operation 1 & 2, a list of tuples - key: value:
    new_list = list(example_1.items())
    # Operation 3: Read keys in a dict
    for key in example_1:
        pass
    # Operation 4: Read keys in a dict
    for key in example_1.keys():
        pass
    # Operation 5: Read values in a dict
    for value in example_1.values():
        pass
    # Operation 6: Overwrites existing keys with second dict, or creates if not there
    example_1 = {1: 'a', 2: 'b', 3: 'c'}
    example_2 = {1: 'aa', 4: 'd'}
    example_1.update(example_2)


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
