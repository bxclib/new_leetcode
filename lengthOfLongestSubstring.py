class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        i = 0 
        j = 0 
        hashmap = {}
        
        res = j-i
        
        while j < len(s):
            if s[j] not in hashmap:
                hashmap[s[j]] = j
                j = j + 1
                res = max(j-i,res)

            else:
                while True:
                    del hashmap[s[i]]
                    i = i + 1
                    if s[j] not in hashmap:
                        break
                    res = max(j-i,res)
                    
        return res
