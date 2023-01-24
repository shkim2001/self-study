class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        dic = collections.Counter()
        
        for item in time:
            
            temp = 60 - (item % 60)
            if temp in dic:
                count += dic[temp]
            if temp == 60:
                dic[temp] += 1
            else:
                dic[item % 60] += 1
        return count
    
#         count = 0
#         for i in range(len(time)):
#             for j in range(i+1, len(time)):
#                 if (time[i] + time[j]) % 60 == 0:
#                     count += 1
                    
#         return count

        