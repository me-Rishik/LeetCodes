class Solution(object):
    def maxArea(self, height):
        left_h,right_h = 0,0
        left_i,right_i = 0,len(height)-1 
        area = 0
        for i in range(len(height)):
            left_h,right_h = height[left_i],height[right_i]
            if min(left_h,right_h)*(right_i-left_i) > area:
                area = min(left_h,right_h)*(right_i-left_i)
            if left_h < right_h:
                left_i += 1
            else:
                right_i -= 1
        return area