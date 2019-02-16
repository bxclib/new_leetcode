class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if p == "":
            return self.tryMatch(s,[]) 
        if len(p) == 1:
            return self.tryMatch(s,[p])
        p_list = []
        jump = False
        for i,j in zip(p[:-1],p[1:]):
            if jump is True:
                jump = False
                continue
            if j == '*':
                p_list.append(i+j)
                jump = True
            else:
                p_list.append(i)
        if jump is False:    
            p_list.append(p[-1])

        return self.tryMatch(s,p_list)

    def tryMatch(self, s:'str', p_list: 'List[str]') -> 'bool':
        if p_list == []:
            if s == '':
                return True
            else:
                return False
        i = p_list[0]
        if len(i) == 2:
            if len(s) == 0:
                return self.tryMatch(s,p_list[1:])
            elif s[0] == i[0] or i[0] == '.':
                return self.tryMatch(s[1:],p_list) or self.tryMatch(s,p_list[1:])
            else:
                return self.tryMatch(s,p_list[1:])
        else:
            if len(s)>0 and len(p_list)>0:
                if i == '.':
                    return self.tryMatch(s[1:],p_list[1:])
                elif i == s[0]:
                    return self.tryMatch(s[1:],p_list[1:])
                else:
                    return False
            elif len(s)==0 and len(p_list)==0:
                return True
            else:
                return False
            
                
            
        
