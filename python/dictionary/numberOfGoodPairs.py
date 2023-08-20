def numGoodPairs(nums):
    pairCount = 0
    map = {}
    for n in nums:
        map[n] = map.get(n, 0) + 1 
        pairCount += map[n] - 1
    return pairCount