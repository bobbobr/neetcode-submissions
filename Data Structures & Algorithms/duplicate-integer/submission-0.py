class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_map = {}
        for i in nums:
            if i not in has_map:
                has_map[i] = 1
            else:
                return True
        return False