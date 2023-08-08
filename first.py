# First question:
# Write a function that takes in a non-empty array of arbitrary intervals,
# merges any overlapping intervals, and returns the new intervals in no particular order.

# Example Input
# = [[1, 2], [3, 5],  [6, 8], [9, 10], [4, 7]]
# Example Output
# = [[1, 2], [3, 8], [9, 10]]

# Avoid confusion;
# [1, 5] [6,7] not overlapping

# [1, 6] [6,7] are -> 1, 7


# HINTS
# 1: The problem asks you to merge overlapping intervals. How can you determine if two intervals are overlapping?
# 2: Sort the intervals with respect to their starting values. This will allow you to merge all overlapping intervals in a single traversal through the sorted intervals.
# 3: After sorting the intervals with respect to their starting values, traverse them, and at each iteration, compare the start of the next interval to the end of the current interval to look for an overlap. If you find an overlap, mutat the current interval so as to merge the next interval into it.
# Optimal Time and Space: O(nlog(n)) time | O(n) space - where n is the length of the input array


# the overal strategy is to iterate over the list and compare the current element with the last output element
def merge_overlapping_intervals(intervals: list):
    output = []

    # sorts the intervals with their first values so we can arrange them together. This is O(n log(n))
    intervals.sort(key=lambda x: x[0])

    # merges the intervals traversing the list. This is O(n) because iterates over the whole list once.
    for interval in intervals:
        # first element? or the last element is not overlapping? -> just adds it to the output
        if not output or interval[0] > output[-1][1]:
            output.append(interval)
        else:
            # the last interval has to be merged with the current one.
            # we keep the first value and update the second value.

            # max and list indexing is O(1)
            output[-1] = output[-1][0], max(output[-1][1], interval[1])

    return output
