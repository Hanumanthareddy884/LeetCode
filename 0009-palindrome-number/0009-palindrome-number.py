class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        b=str(x)
        print(b[::-1])
        if(b==str(b[::-1])):
            return True
        
        return False
        