class Solution:
      def sort(self, arr):
    pointer0 = 0
    pointer2 = len(arr) - 1
    currIndex = 0
    while currIndex <= pointer2:
      if arr[currIndex] == 0:
        arr[pointer0], arr[currIndex] = arr[currIndex], arr[pointer0]
        currIndex += 1
        pointer0 += 1
      elif arr[currIndex] == 1:
        currIndex += 1
      else:
        arr[pointer2], arr[currIndex] = arr[currIndex], arr[pointer2]
        pointer2 -= 1
    return arr
