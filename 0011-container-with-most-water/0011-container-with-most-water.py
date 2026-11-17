class Solution(object):
    def maxArea(self, height):
        left_i,right_i = 0,len(height)-1 
        area = 0
        for i in range(len(height)-1):
            left_h,right_h = height[left_i],height[right_i]
            if left_h < right_h:
                a = min(left_h,right_h)*(right_i-left_i)
                left_i += 1
            else:
                a = min(left_h,right_h)*(right_i-left_i)
                right_i -= 1
            if area < a:
                area = a
        return area