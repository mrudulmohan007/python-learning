"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Example usage:
nums1 = [1, 2, 3, 4]
solution1 = Solution()
result1 = solution1.containsDuplicate(nums1)
print(result1)  # Output: False

nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
solution2 = Solution()
result2 = solution2.containsDuplicate(nums2)
print(result2)  # Output: True

