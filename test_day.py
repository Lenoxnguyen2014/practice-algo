# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#  
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

#output.append(any overlapped that is false, and the result of [smallest, largest])
#compare [1,3] => [2,6] : overlapped : true => [smallest, largets] of the range
# [1,3] => [8, 10] : overlappped: false

#assign [small, large ]

def find_intervals(array):
    output = []
    array = sorted(array)
    for interval in array:
        if len(output) == 0 or output[-1][1] < interval[0]:
            output.append(interval)
        else:
            output[-1][1] = max(output[-1][1], interval[1])
    
    print(output)
    return output

find_intervals([[1,3], [2,6], [8,10], [15,18]])