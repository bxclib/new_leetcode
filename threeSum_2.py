class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        hashmap = {}
        for idx,num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] = hashmap[num] + 1
        res = []
        for idx,num1 in enumerate(nums):
            hashmap_temp = hashmap.copy()
            hashmap_temp = self.del_hash(hashmap_temp,num1)
            for num2 in nums[idx+1:]:
                hashmap_temp = self.del_hash(hashmap_temp,num2)
                if -num1-num2 in hashmap_temp:
                    ans = tuple(sorted([num1,num2,-num1-num2]))
                    if ans not in res:
                        res.append(ans)
        return list(res)
                    
    def del_hash(self,hashmap,num):
        if hashmap[num] == 1:
            del hashmap[num]
        else:
            hashmap[num] = hashmap[num] - 1
        return hashmap
