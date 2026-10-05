class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        try_stack = []
        for temp in range(len(temperatures)):
            if len(try_stack) == 0:
                try_stack.append((temperatures[temp], temp))
            while temperatures[temp] > try_stack[-1][0]:
                remember = try_stack.pop()
                diff = temp - remember[1]
                result[remember[1]] = diff
                print(try_stack)
                print(diff)
                if len(try_stack) == 0:
                    break
            try_stack.append((temperatures[temp], temp))
        print(result)
        return result
