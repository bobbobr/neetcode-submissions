class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0
        for i in range(len(nums)):
            current_center = (start+end) // 2
            print(current_center)
            print(start)
            if nums[current_center]==target:
                return current_center
            elif nums[current_center] > target:
                end = current_center 
            elif nums[current_center] < target:
                start = current_center + 1
        return -1
        