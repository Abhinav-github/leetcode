#Given an integer array nums, find the contiguous subarray within an
#array (containing at least one number) which has the largest product.


class Solution(object):
    def maxProduct(self, nums):
        product=-100000
        min_product = 0
        max_product = 0
        for i in nums:
            if i==0:
                max_product = 0
                min_product = 0
                product = max(product,0)
            elif min_product == 0:
                min_product = i
                max_product =i
                product = max(product,max_product)
            else:
                minpi = min_product*i
                maxpi = max_product*i
                min_product = min(minpi,maxpi,i)
                max_product = max(minpi,maxpi,i)
                product = max(product,max_product,min_product)   
        return product
