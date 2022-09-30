from heapq import *
def find_sum_of_elements(nums, k1, k2):
  # TODO: Write your code here
  minHeap = []
  temp = k2 - k1
  for i in range(len(nums)):
    heappush(minHeap, nums[i])
    if len(minHeap) > temp:
      heappop(minHeap)

  sumAns = 0
  
  for i in range(temp - 1):
    sumAns += heappop(minHeap)


  return sumAns


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
