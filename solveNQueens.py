class Solution:
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        return self.try_next_line([],n)
    def try_next_line(self,tried_part,num_all):
        #print (tried_part)
        ans = []
        if len(tried_part) == num_all:
            # success
            #print (tried_part)
            ans.append(tried_part)
        elif len(tried_part) <= num_all:
            possible_trial = self.g(tried_part,num_all)
            for trial in possible_trial:
                tried_part_temp = tried_part.copy()
                tried_part_temp.append(trial)
                #print (tried_part)
                ans.extend(self.try_next_line(tried_part_temp,num_all))
        #print ("ans",ans)
        return ans
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
