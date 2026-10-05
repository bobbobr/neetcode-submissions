class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        start, end = 0, len(nums)-1
        sol = []
        uniq_sol = set()
        for k in range(start, len(nums)):
            print(start)
            end = len(nums)-1
            for j in range(end, start, -1):
                for i in range(start+1, end):
                    print(start+1, end)
                    print(i)
                    print(nums[start], nums[i], nums[j])
                    if (nums[i] + nums[start] + nums[j]) == 0:
                        add_list= [nums[start], nums[i], nums[j]]
                        add_list.sort()
                        if add_list not in sol:
                            sol.append(add_list)
                end-=1
            start+=1
        return (sol)
        