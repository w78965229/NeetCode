'''
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

'''


def hasDuplicate( nums):
    '''解法1'''
    hash_set = set()
    for n in nums:
        if n in hash_set:
            return True

        hash_set.add(n)
    return False
    '''解法2'''

    # if len(nums) == len(set(nums)):
    #     return False
    # else:
    #     return True

def main():
    test_case = [1, 2, 3]

    hasDuplicate(test_case)

if __name__ == "__main__":
    main()


