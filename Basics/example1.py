class Solution:
    def pivotIndex(self):
        nums = [2,1,-1]
        left = 0
        right=sum(nums)

        for x,value in enumerate(nums):
            right -= value
            if right == left:
                return x

            left+=value

        return -1


