from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):

  minHeap = []
  # TODO: Write your code here
  for i in range(len(ropeLengths)):
    heappush(minHeap, ropeLengths[i])

  result = 0

  while len(minHeap) > 1:
    temp = heappop(minHeap) + heappop(minHeap)
    result += temp
    heappush(minHeap, temp)
    
  return result

def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
