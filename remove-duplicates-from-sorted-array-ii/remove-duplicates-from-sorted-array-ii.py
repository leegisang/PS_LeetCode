class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = [nums[0]] * n
        index = 1
        is_duplicated = False
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                if not is_duplicated:
                    l[index] = nums[i+1]
                    index += 1
                    is_duplicated = True
            else:
                l[index] = nums[i+1]
                index += 1
                is_duplicated = False

        nums[:len(l)] = l
        
        return index