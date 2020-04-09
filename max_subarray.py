from sys import maxsize


# print largest contiguous sub array sum using dynamic programming
def maxSubArrayDynamicProgram(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


# print largest contiguous sub array sum
def maxSubArraySumStartEndIndex(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print('Max Sub array sum %d' % (max_so_far))
    print('Start index is here %d' % (start))
    print('End index is here %d' % (end))


a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySumStartEndIndex(a, len(a))
print('Max Sub array sum dynamic programming ', maxSubArrayDynamicProgram(a, len(a)))
