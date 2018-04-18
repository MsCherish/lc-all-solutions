class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}                         #用于存储｛值：对应序列｝
        for i, num in enumerate(nums):  #遍历数组中的索引和对应的元素值
            if target - num in d:        #直接在d中看其补值在不在d中，如果在直接返回补值的索引和当前考察的索引i
                return [d[target - num], i]
            d[num] = i
        # no special case handling becasue it's assumed that it has only one solution
            
