import collections
from heapq import *

def find_maximum_distinct_elements(nums, k):
      minHeap = []
      dic = collections.Counter()
      for num in nums:
            dic[num] += 1
      count = 0
      for num, freq in dic.items():
            if freq == 1:
                  count += 1
            else:
                  heappush(minHeap, (freq, num))

      while k > 0 and minHeap:
            freq, num = heappop(minHeap)
            k -= freq - 1
            if k >= 0:
                  count += 1
      
      if k > 0:
            count -= k
      
      return count


def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()

