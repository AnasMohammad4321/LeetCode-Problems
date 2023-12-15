class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif bracket in brackets.values():
                if not stack or brackets[stack.pop()] != bracket:
                    return False
            else:
                return False

        return not stack