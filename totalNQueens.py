class Solution:
    def totalNQueens(self, n: 'int') -> 'int':
        stack = []
        ans = []
        stack.append([])
        while stack != []:
            tried = stack.pop()
            if len(tried) == n:
                ans.append(tried)
            else:
                trial_list = self.g(tried,n)
                if trial_list != []:
                    for trial in trial_list:
                        stack.append(tried+[trial])
        return len(ans)
    def g(self,tried_part,num_all):
        n = len(tried_part)
        banned_area = []
        ans = []
        for i,line in enumerate(tried_part):
            k = line.index('Q')
            banned_area.extend([k-(n-i),k,k+(n-i)])
        for i in range(num_all):
            if i not in banned_area:
                s_temp = "."*i + 'Q' + "."*(num_all-i-1)
                ans.append(s_temp)
        return ans     
