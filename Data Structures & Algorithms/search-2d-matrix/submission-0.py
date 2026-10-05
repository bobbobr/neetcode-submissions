class Solution:

    def binary_search_test(self, row_try, target):
        left, right = 0, len(row_try)-1
        mid = left + (right - left // 2)
        print(row_try)
        for mid in range(len(row_try)):
            print(mid)
            
            if row_try[mid] == target:
                return True
            elif row_try[mid] < target:
                left = row_try[mid] + 1 
            elif row_try[mid] > target:
                right = row_try[mid] - 1 
        return False 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:    
        for row in matrix:
            if self.binary_search_test(row,target):
                return True
        return False
                
             

        