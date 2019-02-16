class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        point = len(nums) - 1

        for idx,num in enumerate(nums):
            while nums[point] == val:
                point = point - 1
                if point < 0:
                    return 0
            if nums[idx] == val:    
                if idx < point:
                    nums[idx] = nums[point]
                    nums[point] = val
                else:
                    return point + 1
