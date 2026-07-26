class Solution:
    def maximumProduct(self, nums):
        nums.sort()

        # Product of three largest numbers
        product1 = nums[-1] * nums[-2] * nums[-3]

        # Product of two smallest (possibly negative) and the largest
        product2 = nums[0] * nums[1] * nums[-1]

        return max(product1, product2)