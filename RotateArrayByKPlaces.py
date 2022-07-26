class Solution(object):
    '''Time complexity: O(n)
    Space Complexity : O(1)'''
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end]=nums[end], nums[start]
            start+=1
            end-=1
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        
        #Reverse whole array
        self.reverse(nums, 0, n-1)
        #Reverse first n-k elements
        self.reverse(nums, 0, k-1)
        #Reverse rest
        self.reverse(nums, k, n-1)
        
        
