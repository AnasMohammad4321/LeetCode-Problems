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
        steps[0] = 1
        steps[1] = 1
        
        for i in range(2, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]