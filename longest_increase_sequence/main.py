from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)

        for current_index in range(len(nums) - 1, -1, -1):
            for next_index in range(current_index + 1, len(nums)):
                if nums[current_index] < nums[next_index]:
                    lengths[current_index] = max(lengths[current_index], 1 + lengths[next_index])

        return max(lengths)