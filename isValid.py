class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack = []
        for i in s:
            #print (stack)
            #print (i)
            if i =='(' or i == '[' or i == '{':
                stack.append(i)
                #print ("yes")
                #print (stack)
            else:
                if i == ')':
                    #print ("1 case")
                    if stack == []:
                        return False
                    if stack.pop() != '(': 
                        return False
                if i == ']':
                    #print ("2 case")
                    if stack == []:
                        return False
                    if stack.pop() != '[': 
                        return False
                if i == '}':
                    #print ("3 case")
                    if stack == []:
                        return False
                    if stack.pop() != '{': 
                        return False 
                    
        if stack == []:
            return True
        else:
            return False
