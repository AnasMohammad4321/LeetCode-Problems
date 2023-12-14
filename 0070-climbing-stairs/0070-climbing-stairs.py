class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 1
        
        steps = []
        for i in range(n+1):
            steps.append(0)
        zero = 1
        one = 1
        
        for i in range(2, n+1):
            nest = zero + one
            zero = one
            one = nest
            
        return nest