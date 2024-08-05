class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        d=[]
        for i in arr:
            a=arr.count(i)
            if a==1:
                d.append(i)
        if k-1>len(d):
            return ""
        else:
            return d[k-1]
        