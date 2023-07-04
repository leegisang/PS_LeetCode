class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k != 0:
            a, b = nums[-k:], nums[:-k]
            nums[:k] = a
            nums[k:] = b
            # print(nums)