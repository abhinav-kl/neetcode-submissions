class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # val -> index

        for index, num in enumerate(nums):
            indices[num] = index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in indices and indices[diff] != index:
                return [index, indices[diff]]

        return []