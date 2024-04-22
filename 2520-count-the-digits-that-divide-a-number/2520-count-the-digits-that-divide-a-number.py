class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        stri = str(num)
        result = 0
        for single in stri:
            if num % int(single) == 0:
                result += 1
        return result
        