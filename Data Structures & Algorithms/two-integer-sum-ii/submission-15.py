class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(numbers)):
            for j in numbers[i+1:]:
                print(numbers[i] + j)
                print(numbers)
                if (numbers[i] + j) == target:
                    return [i+1,numbers.index(j)+1]
            # numbers = numbers[i+1:]