class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        l = 0
        r = len(height)-1
        left_max = 0
        right_max = 0
        while l < r:
            left_max = max(left_max,height[l])  #item with max height from left
            right_max = max(right_max,height[r])    #item with max height from right
            if left_max <= right_max:
                water += (left_max - height[l])     #water level = min(left_max,right_max) - height(i) 
                
                l += 1
            else:
                water += (right_max - height[r])
                
                r -= 1
        return water
        