from heapq import *


def find_k_largest_numbers(nums, k):
  minHeap = []
  # More optimal Solution O(K * logn + (N-K) * logn)
  for i in range(k):
    heappush(minHeap, nums[i])
  
  for j in range(k, len(nums)):
    if nums[j] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[j])
  
  return minHeap

  # O(nlogn) solution
  # result = []
  # nums = sorted(nums)[::-1]
  # for i in range(k):
  #   result.append(nums[i])
  # return result


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
