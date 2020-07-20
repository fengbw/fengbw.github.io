#Subsets
class Solution(object):
    def subsets(self, nums):
        if not nums:
            return [[]]
        nums = sorted(nums)
        self.res = []
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, index, subset):
        self.res.append(list(subset))

        for i in range(index,len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i+1, subset)
            subset.pop()

s = Solution()
nums = [1,2,3]
print(s.subsets(nums))
