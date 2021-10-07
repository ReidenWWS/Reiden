class Solution:
    def solve(self, nums):
        x = set()
        for i in nums:
            if i in x:
                return i

            
            
            else:
                x.add(i)