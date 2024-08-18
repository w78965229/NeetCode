'''
Two Integer Sum
Solved
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
'''


def twoSum( nums, target) :
    '''解法一'''
    hash_set = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in hash_set:
            return [hash_set[diff], i]

        hash_set[n] = i

    '''解法二'''
    key = target

    for i in range(len(nums) - 1):
        key = target - nums[i]

        for j in range(i + 1, len(nums)):

            if nums[j] == key:
                return [i, j]

    return False

def main():
    nums = [3,4,5,6]
    target = 7

    flag=twoSum(nums,target)
    print(f"flag='{flag}'")
if __name__ == "__main__":
    main()

