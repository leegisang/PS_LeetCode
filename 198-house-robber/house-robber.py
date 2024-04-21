class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        elif n == 3:
            poss0 = max(nums[1], sum([nums[0], nums[2]]))
            return poss0
        else:
            poss0 = max(nums[1], sum([nums[0], nums[2]]))
            for i in range(3, n):
                poss1 = nums[i-3] + nums[i-1]
                poss2 = nums[i-2] + nums[i]
                poss3 = nums[i-3] + nums[i]
                if i >= 5:
                    poss4 = nums[i-5] + nums[i]
                    max_p = max(poss0, poss1, poss2, poss3, poss4)

                else:
                    poss4= 0
                    max_p = max(poss0, poss1, poss2, poss3)
                print(nums)
                print(nums[i-3:i+1])
                print(poss0)
                print(poss1, poss2, poss3)
                print(poss4)
                print(max_p)
                print()
                if poss0 == max_p:
                    nums[i-1] = max_p
                else:
                    nums[i-1] = poss1
                nums[i-3] = max_p
                poss0 = max_p
        return max_p
