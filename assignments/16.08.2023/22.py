class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        result = []
        
        for i in range(2 ** (2 * n)):
            current = bin(i)[2:].zfill(2 * n)
            left_count = right_count = 0
            valid = True
            temp = ""
            
            for char in current:
                if char == '0':
                    temp += "("
                    left_count += 1
                else:
                    temp += ")"
                    right_count += 1
                    
                if right_count > left_count:
                    valid = False
                    break
            
            if valid and left_count == n and right_count == n:
                result.append(temp)
        
        return result