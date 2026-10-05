class Solution:
    def finish_or_not(self, k, piles, max_hours):
        passed = 0
        for i in piles:
            if i % k ==0:
                passed += (i//k )
            else:
                passed += (i//k + 1)
        if passed <= max_hours:
            return True
        else: 
            return False
        #return True if passed <= max_hours else False
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right  

        while left <= right:
            mid = (left + right) // 2
            if self.finish_or_not(mid, piles, h):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
    


            