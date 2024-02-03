# @chrisbuild124
# This is Bubble Sort and uses matplotlib to visualize it.
# Your machine must have matplotlib installed to run this.
# Run the program and input number of objects desired (1-50 objects)
# to be in order and how fast to iterate (0.5-5 seconds).
# --------------------------------------Description--------------------------------------

import matplotlib.pyplot as plt
import random


def main():
    """
    Description: This is the main function for the program.
    """
    bar_number, time_interval = input_bubble_sort()
    random_list = generate_random_list(bar_number)
    bubble_sort(random_list, time_interval)


# Input the bar number. Must be an integer from 1-50 inclusive.
def input_bubble_sort():
    """
    Description: This is the main function for the program.

    params:      Void.

    :returns:    The number of different numbers to sort.
    """
    bar_number = -1
    while bar_number < 1 or bar_number > 50 or not isinstance(bar_number, int):
        try:
            bar_number = int(input("Number of groups to sort: "))
        except TypeError:
            pass
        except ValueError:
            pass
        if bar_number < 1 or bar_number > 100 or not isinstance(bar_number, int):
            print("Must be an integer between 1-50 inclusive. Try again.")

    time_interval = -1
    while time_interval < 0.25 or time_interval > 5 or not isinstance(time_interval, float):
        try:
            time_interval = float(input("Time between iterations: "))
        except TypeError:
            pass
        except ValueError:
            pass
        if time_interval < 0.25 or time_interval > 5 or not isinstance(time_interval, float):
            print("Must be a float between 0.25-5 inclusive. Try again.")
    return bar_number, time_interval


# Bubble Sort Loop
def generate_random_list(length):
    """
    Description: This generates a random list of numbers with a length of length.

    :param       length - An integer for how many numbers to randomize.

    :returns:    random_list - A list with the numbers randomized.
    """
    start = 1
    end = length
    random_list = [random.randint(start, end) for _ in range(length)]
    return random_list


def bubble_sort(height_list, time_interval):
    """
    Description:        Bubble sort and graphs the output.

    :param height_list: The y values of the graph.
    :param time_interval: The time between iterations.

    :returns:           None
    """
    # -1 is the start and j is each next iteration.
    for i in range(len(height_list)):
        graph(-1, height_list, time_interval)
        for j in range(len(height_list) - 1 - i):
            if height_list[j] > height_list[j+1]:
                buffer = height_list[j+1]
                height_list[j+1] = height_list[j]
                height_list[j] = buffer
            graph(j, height_list, time_interval)


def graph(j, height_list, time_interval):
    """
    Description:          This graphs the function and is displayed
                          each time it is called.

    :param j:             Choose to highlight blue which element.
    :param height_list:   A list of the y values.
    :param time_interval: Time between iterations.

    :returns:             Nothing but displays.
    """
    bar_colors = ['#8a2be2' for _ in range(len(height_list))]
    x_coordinates = list(range(len(height_list)))
    plt.clf()
    # Must be -1 since it skips the index 1 term.
    if j == -1:
        bar_colors[0] = '#40e0d0'
    else:
        bar_colors[j], bar_colors[j+1] = '#8a2be2', '#40e0d0'
    # Plots the chart. Removes x/y ticks, can override the previous chart, and pauses.
    plt.bar(x_coordinates, height_list, color=bar_colors)
    plt.title('Bubble Sort Visualization by @chrisbuild124')
    plt.xticks([])
    plt.yticks([])
    plt.show(block=False)
    plt.pause(time_interval)


if __name__ == '__main__':
    main()
