import collections
from heapq import *

def sort_character_by_frequency(str):
  # TODO: Write your code here
  dic = collections.Counter()
  
  for i in range(len(str)):
    dic[str[i]] += 1
  minHeap = []
  for char, freq in dic.items():
    heappush(minHeap, (-freq, char))
  temp = ""

  while minHeap:
    temp1 = heappop(minHeap)
    temp += temp1[1] * -temp1[0]

  return temp


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
