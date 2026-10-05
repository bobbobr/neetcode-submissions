class Solution:
    def findMin(self, nums: List[int]) -> int:
        right, left = 0, len(nums)-1
        current_min = nums[0]
        # if abs((nums[left] - nums[right])) == left:
        #     if nums[left] > nums[right]:
        #         print(nums[left])
        #         current_min = nums[right]
        #     else:
        #         print(nums[left])
        #         current_min = nums[left]
        while right <= left:
            if nums[right] < nums[left]:
                current_min = min(current_min, nums[right])
                break
            mid = right + (left - right) // 2
            if current_min >= nums[mid]:
                current_min = nums[mid]
            if nums[mid] >= nums[right]:
               right = mid + 1
            else:
                left = mid - 1 
        return current_min