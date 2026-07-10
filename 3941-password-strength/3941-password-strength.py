class Solution(object):
    def passwordStrength(self, password):
        d = set()
        ans = 0
        for char in password:
            if char in d:
                continue
            d.add(char)
            if char.islower():
                ans+=1
            elif char.isupper():
                ans+=2
            elif char.isdigit():
                ans+=3
            else:
                ans+=5
        return ans