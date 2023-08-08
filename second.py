# You're given an array of non-negative integers where each non-zero integer represents the height of a
# pillar of width 1. Imagine water being poured over all of the pillars; write a function that returns
# the surface area of the water trapped between the pillars viewed from the front. Note that spilled water
# should be ignored.

# Sample Input
#  = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
#
#             water
#            \    /
#             \  /
#              \/
#
#               #
#               #
#         #~~~~~#
#         #~~~~~#
#         #~~~~~#
#         #~~#~~#
#         #~~#~~#
#         #~~#~~#~~~~~#
#         #~~#~~#~~~~~#
#        _#~~#~~#~~##~#
#
#  Sample Output = 48
#
#
#

# HINTS:
# 1: In order to calculate the amount of water above a single point in the input array,
#    you must know the height of the tallest pillar to its left and the height of the tallest pillar to its right.
# 2: If a point can hold water above it, then the smallest of the two heights mentioned in Hint #1 minus
#    the height at that respective point should lead you to the amount of water above it.
# 3: Try building an array of the left and right max heights for each point in the input array.
#    You should be able to build this array and to compute the final amount of water above each point in just
#    two loops over the input array.


def area_of_the_water_trapped(pillars):
    # first we calculate the left and right tallest pillars
    pillars_count = len(pillars)
    left_tallest_pillars = [0] * pillars_count
    right_tallest_pillars = [0] * pillars_count

    # first we calculate the left tallest pillars
    for i in range(1, pillars_count):
        left_tallest_pillars[i] = max(pillars[0:i])

    # then we calculate the right tallest pillars
    for i in range(0, pillars_count - 1):
        right_tallest_pillars[i] = max(pillars[i + 1 : pillars_count])

    amount_of_water = [0] * pillars_count
    area = 0
    for i in range(pillars_count):
        smallest_of_the_two_heights = min(left_tallest_pillars[i], right_tallest_pillars[i])
        # amount of water above the pillar is the difference between the smallest of the two heights and the height of the pillar
        # could be negative as well so we clamp it to zero
        amount_of_water[i] = max(0, smallest_of_the_two_heights - pillars[i])
        area += amount_of_water[i]

    return area
