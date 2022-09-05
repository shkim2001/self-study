class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        rPtr = len(S) - 1
        ans = ''
        for ch in S:
            if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
                while(rPtr > 0 and (S[rPtr] < 'a' or S[rPtr] > 'z') and (S[rPtr] < 'A' or S[rPtr] > 'Z')):
                    rPtr -= 1
                ans += S[rPtr]
                rPtr -= 1
            else:
                ans += ch
        return ans