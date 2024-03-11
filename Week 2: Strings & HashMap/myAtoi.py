class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: 
            return 0
        
        s = s.strip() #remove leading/trailing whitespace uniform input 
        
        sol = 0
        window = 0 
        sign = 1

        while window < len(s) and s[window].isalpha():
            window += 1
        
        while window < len(s) and s[window] == "-":
            sign = -1
            window += 1
        
        while window <len(s) and s[window].isdigit():
            sol = sol * 10 + int(s[window])
            window += 1

        return sol * sign
