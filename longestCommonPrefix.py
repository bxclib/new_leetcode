class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if strs == []:
            return ""
        lmin = min([len(s) for s in strs])
        idx = 0 
        ans = []
        while idx < lmin:
            temp = []
            for s in strs:
                temp.append(s[idx])
            print (temp)
            if len(set(temp)) == 1:
                ans.append(s[idx])
            else:
                break
            idx = idx + 1
        return "".join(ans)
        
