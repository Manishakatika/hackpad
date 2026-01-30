class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        result = [-1] * n
        for i, num in enumerate(nums):
            while stack and num > stack[-1][0]:
                top = stack.pop()
                result[top[1]] = num
            stack.append((num, i))
        
        j = 0
        while j < n - 1 and len(stack) > 1:
            while len(stack) > 1 and nums[j] > stack[-1][0]:
                result[stack.pop()[1]] = nums[j]
            j += 1

        return result
