"""
When it rains it pours
(Level 3, Problem 2)
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held,
but a sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to
house the fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from
Professor Boolean's lab, you must compute how much standing water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and
allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of
this problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list,
computes the total area of standing water accumulated when water is poured from the top and allowed to run off the
sides.

The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least
1, and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0
"""


def check_if_will_hit_wall(heights, position):
    origin_height = heights[position]
    wall_found = False
    for next_height in heights[position + 1::]:
        if not origin_height > next_height:
            wall_found = True
            break
    return True if wall_found else False


def fill_in_water_and_return_weight(heights, last_checked_height=None):
    water_weight = 0
    position = 0
    while position < len(heights) - 1:
        origin_height = heights[position]
        if check_if_will_hit_wall(heights, position):
            potential_water_fill = 0
            next_column_index = position + 1
            while next_column_index <= len(heights) - 1:
                next_column_height = heights[next_column_index]
                if origin_height > next_column_height:
                    potential_water_fill += origin_height - next_column_height
                    next_column_index += 1
                else:
                    water_weight += potential_water_fill
                    break
            position = next_column_index
        else:
            if origin_height == last_checked_height:
                break
            else:
                water_weight += fill_in_water_and_return_weight(heights[len(heights) - 1:position - 1:-1],
                                                                origin_height)
                break
    return water_weight


def answer(heights):
    return fill_in_water_and_return_weight(heights)
