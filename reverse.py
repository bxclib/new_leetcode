class Solution:
    def reverse(self, x: 'int') -> 'int':
        x = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])   
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x
