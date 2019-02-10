class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows == 1:
            return s
        ans = []
        for i in range(numRows):
            ans.append([])
        i = 0
        j = 0
        flag = 0
        #print (ans)
        for c in s:
            ans[j].append(c)
            #print (i,j)
            if flag == 0:
                j = j + 1
            else:
                i = i + 1
                j = j - 1
            if j == numRows - 1:
                flag = 1 
            if j == 0:
                flag = 0

        
        res = []
        for i in ans:
            res.extend(i)
        return "".join(res)
