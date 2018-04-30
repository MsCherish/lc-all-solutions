class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
            
        return ans
    
    
    
        """使用两个字典记录下两个数组中元素出现的次数"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1,dic2 = dict(),dict()
        for num in nums1:
            dic1[num] = dic1.get(num,0) + 1
        for num in nums2:
            dic2[num] = dic2.get(num,0) + 1
        return [x for x in dic2 for j in range(min(dic1.get(x,0),dic2.get(x,0)))]

"""但是python内置了Counter类型数组，可以方便实现计数功能"""
import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1,c2 = collections.Counter(nums1),collections.Counter(nums2)
        return [i for i in c1.keys() for j in range(min([c1[i], c2[i]]))]
