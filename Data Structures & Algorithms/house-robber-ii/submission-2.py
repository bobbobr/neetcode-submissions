class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        dp = [0] * (len(nums) + 2)
        dp2 = [0] * (len(nums) + 2)

        for i in range(len(nums)-1):
            dp[i+2] = max(dp[i+1], dp[i] + nums[i])

        for i in range(1, len(nums)):
            dp2[i+2] = max(dp2[i+1], dp2[i] + nums[i])


        return max(max(dp), max(dp2))
        