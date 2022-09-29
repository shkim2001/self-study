import collections
from heapq import *

def find_k_frequent_numbers(nums, k):
  dic = collections.Counter()
  for num in nums:
    dic[num] += 1

  maxHeap = []
  
  for num, freq in dic.items():
    heappush(maxHeap, (freq,num))
    if len(maxHeap) > k:
      heappop(maxHeap)
  topNumbers = []
  while maxHeap:
    topNumbers.append(heappop(maxHeap)[1])
  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
