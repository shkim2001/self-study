class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = collections.Counter()
        start = 0
        maxLen = 0
        # TODO: Write your code here
        for i in range(len(fruits)):
            dic[fruits[i]] += 1
            while len(dic) > 2:
                temp = fruits[start]
                dic[temp] -= 1
                if dic[temp] == 0:
                    del dic[temp]
                start += 1
            maxLen = max(maxLen, i - start + 1)

        return maxLen