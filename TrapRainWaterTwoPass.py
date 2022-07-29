class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''We need to perform 2 passes
        // Forward pass
        1. Take 2 pointers, slow and fast, and update the current trapped water if height of fast is less than height of slow. 
        2. Else update the result, slow to fast and update current trapped water to 0
        
        // Backward pass
        1. Set the peak value to the last slow 
        2. Reset current trapped water
        3. slow = n-1 and fast= slow-1
        4. update the current trapped water if height of fast is less OR EQUAL to the height of slow. Why equal? because, if s=f, te water will be counted twice, once in forward pass and once in backward pass
        5. Else update the result, slow to fast and update current trapped water to 0
        '''
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        #Edge case
        if len(height)==0 or len(height)==1:
            return 0
        
        #Take 2 pointers
        slow = 0
        fast = 1
        
        final_result=0
        current_trapped=0
        
        peak=0
        for i in range(len(height)):
            if height[i] >=height[peak]:
                peak=i
        
        #Forward pass
        while fast<=peak:
            if height[fast]<height[slow]:
                current_trapped+=height[slow]-height[fast]
            else:
                final_result+=current_trapped
                slow=fast
                current_trapped=0
            fast+=1
            
        #Backward pass
        slow=len(height)-1
        fast=slow-1
        current_trapped=0
        while fast>=peak:
            if height[fast]<=height[slow]:
                current_trapped+=height[slow]-height[fast]
            else:
                final_result+=current_trapped
                slow=fast
                current_trapped=0
            fast-=1
        return final_result
        
