class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        s = s.replace("?","")
        s = s.replace(".","")
        s = s.replace(",","")
        s = s.replace("'","")
        s = s.replace(":","")

        for i in range(len(s)):
            n = len(s)
            if s[i] != s[n-i-1]:
                return False
        return True
            

        