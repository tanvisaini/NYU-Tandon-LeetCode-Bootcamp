class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(word):
            return word == word[::-1]
        
        sol = []
        curr = 0
        for item in words:
            while i < len(words): 
                # completely stumped, not sure what to do from here