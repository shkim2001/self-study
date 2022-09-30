from heapq import *

def find_closest_elements(arr, K, X):
      result = []
      minHeap = []
      for i in range(len(arr)):
            temp = abs(arr[i] - X)
            heappush(minHeap, (temp, arr[i]))

      for i in range(K):
            result.append(heappop(minHeap)[1])   

      return sorted(result)


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
