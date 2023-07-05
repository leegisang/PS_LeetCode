class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # from collections import Counter
        # val, count = Counter(nums).most_common()[0]
        # if count > len(nums) / 2:
        #     return val
        # else:
        #     return -1
        nums.sort()
        return nums[len(nums)//2]
    # 정렬하고 가운데 엘리먼트 리턴