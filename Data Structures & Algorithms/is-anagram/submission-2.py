class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasmap_s = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in hasmap_s:
                hasmap_s[i] = 1
            else:
                hasmap_s[i] += 1
        for j in t:
            if j not in hasmap_s:
                return False
            else:
                hasmap_s[j] -=1
                if hasmap_s[j] < 0:
                    return False
        return True        
        