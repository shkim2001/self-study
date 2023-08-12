import math


class Solution:
    def findLength(self, fruits):
        max_length = 0
        startIndex = 0
        counter = {}

        for i in range(len(fruits)):
            if fruits[i] not in counter:
                counter[fruits[i]] = 0
            counter[fruits[i]] += 1

            while len(counter) > 2:
                counter[fruits[startIndex]] -= 1
                if counter[fruits[startIndex]] == 0:
                    del counter[fruits[startIndex]]
                startIndex += 1

            max_length = max(max_length, i - startIndex + 1)

        return max_length
