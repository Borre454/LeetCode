class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
        
# Test
solution = Solution()
print(solution.removeDuplicates([1,1,4,4,5])) # Should be 3