class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        hashmap =  [('M' , 1000),
                   ('CM' , 900),
                   ('D' , 500),
                   ('CD' , 400),
                   ('C' , 100),
                   ('XC' , 90),
                   ('L' , 50),
                   ('XL' , 40),
                   ('X' , 10),
                   ('IX', 9),
                   ('V' , 5),
                   ('IV' , 4),
                   ('I' , 1)]
        hashmap = dict(hashmap)

        if len(s) == 1:
            return hashmap[s]
        
        ans = 0
        jump = 0 
        
        for c1,c2 in zip(s[:-1],s[1:]):
            if jump == 1:
                jump = 0
                continue
            if hashmap[c1] >= hashmap[c2]:
                ans = ans + hashmap[c1]
                #print (c1)
            else:
                ans = ans + hashmap[c1+c2]
                jump = 1
                #print (c1+c2)
        if jump == 0:        
            ans = ans + hashmap[c2]
        
        return ans
