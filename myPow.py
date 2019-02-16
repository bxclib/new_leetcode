class Solution:
    def myPow(self, x: 'float', n: 'int') -> 'float':
        if x == 0 :
            return 0
        elif n > 0:
            p = n//2
            s = pow(x,p)
            if n%2 == 0:
                return s*s
            else:
                return s*s*x
        elif n == 0:
            if x!=0:
                return 1
        elif n < 0:
            return pow(1/x,-1*n)
