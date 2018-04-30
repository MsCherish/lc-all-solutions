class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        ans = []
        for num in nums1:       #用hash table保存下数组1的出现的元素
            d[num] = d.get(num, 0) + 1  #值记录元素出现的次数
        
        for num in nums2:
            if num in d:
                ans.append(num)
                del d[num]
        return ans
    
    
         """可以使用hash table保存下数组1的出现的元素，然后判断数组2中的各元素是否在数组1中出现过，但直接使用set更简单"""
        nums1 = set(nums1)
        return [x for x in set(nums2) if x in nums1] 
