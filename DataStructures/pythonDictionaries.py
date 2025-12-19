# @chrisbuild124
# These are some Python built in data Structures and notes.
# This includes: Dictionary
# --------------------------------------Description--------------------------------------

import collections

def main():
    """
    Description: This is the main function for the program.
    """
    dictionaries()

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

if __name__ == '__main__':
    main()
