# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

from collections import Counter


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window = 0
        dict =[]
        maxFreq = 0
        differs = 0
        start = 0

        for i, num in enumerate(s):
            dict[num] = dict.get(num, 0) + 1
            maxFreq = max(maxFreq, dict[num])
            differs = 1 - maxFreq
            if differs > k: 
                dict[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen
            

