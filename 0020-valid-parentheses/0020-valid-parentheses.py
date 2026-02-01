class Solution(object):
    def isValid(self, s):
        pairs ={')':'(',']':'[', '}':'{' }
        stack = []
        for val in s:
            if val in pairs.values():
                stack.append(val)
            elif val in pairs.keys():
                if not stack or pairs[val] != stack.pop():
                    return False
        return not stack
                    

        