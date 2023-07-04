class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        val, count = Counter(nums).most_common()[0]
        if count > len(nums) / 2:
            return val
        else:
            return -1