class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has_l = {}
        ans = []
        for i in strs:
            ans_1 = []
            for j in strs:
                if sorted(i) == sorted(j):
                    if j not in ans:
                        ans_1.append(j)
            if ans_1 not in ans:
                ans.append(ans_1)
        print(ans)   
        return ans