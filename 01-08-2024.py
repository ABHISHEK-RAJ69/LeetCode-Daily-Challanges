class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count=0
        for a in details :
            age=int(a[-4]+a[-3])
            if age >60:
                count+=1
        return count
        