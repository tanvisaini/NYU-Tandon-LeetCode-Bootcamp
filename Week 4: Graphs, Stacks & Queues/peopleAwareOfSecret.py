class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        known = 1  # The first person knows the secret initially

        for day in range(delay, n + 1):
            known = (known + known) % MOD
            
            if day - forget > 0:
                known = (known - (known - 1) // (day - forget) - 1) % MOD

            if day - delay > 0:
                known = (known + known - 1) % MOD

        return known