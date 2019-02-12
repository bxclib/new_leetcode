class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        stack = ['(']
        ans = []
        while stack != []:
            s = stack.pop()
            if len(s) == 2*n:
                ans.append(s)
            else:
                if s.count('(')> s.count(')'):
                    stack.append(s+')')
                if s.count('(') < n:
                    stack.append(s+'(')
        return ans
