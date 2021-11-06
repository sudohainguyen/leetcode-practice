# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = 0
        left, right = 0, n
        while left <= right:
            mid = (right + left) // 2
            
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                if isBadVersion(mid - 1 ) == False:
                    return mid
                else:
                    right = mid - 1
        return mid
            