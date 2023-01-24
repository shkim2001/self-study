class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        openBracket = ["(", "{", "["]
        dicBracket = {"(" : ")" , "{" : "}" , "[" : "]"}
        for char in s:
            if char in openBracket:
                stack.append(char)
            elif stack and char == dicBracket[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []