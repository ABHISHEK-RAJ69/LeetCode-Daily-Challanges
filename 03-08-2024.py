class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        k=tuple(arr)
        # copy of arr 
        for b in k:
            if b in target :
                target.remove(b)
                arr.remove(b)
            else:
                return False
        if target==[]and arr==[]:
            return True 
        else:
            return False