class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            print(left,right)
            mids = left + (right-left) // 2
            print(nums[mids])
            if target == nums[mids]:
                return mids
                break
            # elif target < nums[left]:
            #     left = mids + 1
            if nums[left] <= nums[mids]:
                if target > nums[mids] or target < nums[left]:
                    left = mids + 1
                else:
                    right = mids - 1 
            else:
                if target < nums[mids] or target > nums[right]:
                    right = mids - 1
                else:
                    left = mids + 1 
        if nums[mids] == target:
            return mids 
        else:
            return -1   
        