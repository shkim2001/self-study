import math


class Solution:
    def shortestDistance(self, words, word1, word2):
        shortestDistance = len(words)
        position1, position2 = -1, -1  
        for i, word in enumerate(words):
            if word == word1:  
                position1 = i
            elif word == word2: 
                position2 = i
            if position1 != -1 and position2 != -1:
                shortestDistance = min(
                    shortestDistance, abs(position1 - position2))

        return shortestDistance
