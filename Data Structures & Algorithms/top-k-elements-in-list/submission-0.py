class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for idx, value in count.items():
            freq[value].append(idx)

        res = []
        for idx in range(len(freq) - 1, 0, -1):
            for num in freq[idx]:
                res.append(num)
                if len(res) == k:
                    return res