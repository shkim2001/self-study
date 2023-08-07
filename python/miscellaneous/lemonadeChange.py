class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        price = 5
        billCount = collections.Counter()
        
        for i in range(len(bills)):
            billCount[bills[i]] += 1
        
            if bills[i] == 10:
                if billCount[5] > 0:
                    billCount[5] -= 1
                else:
                    return False
            if bills[i] == 20:
                if billCount[5] > 0 and billCount[10] > 0:
                    print(i, billCount[5] > 2)
                    billCount[5] -= 1
                    billCount[10] -= 1
                elif billCount[5] > 2:
                    billCount[5] -= 3
                else:
                    return False
        
        return True