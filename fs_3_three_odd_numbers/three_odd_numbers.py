def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    sum = 0
    for i in range(len(nums)):
        if len(nums[i: i + 3]) < 3:
            break
        for j in nums[i: i + 3]:
            sum += j
        if sum % 2 == 0:
            sum = 0
        else:
            return True
    return False
