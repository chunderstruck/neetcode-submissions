class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = 0
        for i, outer_num in enumerate(nums):
            for j, inner_num in enumerate(nums):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]
                    
