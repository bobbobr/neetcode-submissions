class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()

        def dfs(start, current, total):
            if total == target:
                res.append(current.copy())
                return 

            for i in range(start, len(candidates)):
                if candidates[i] == candidates[i-1] and i > start:
                    continue

                if total > target:
                    return 

                current.append(candidates[i])

                dfs(i+1, current, total + candidates[i])

                current.pop()


        dfs(0,[], 0)

        return res
        