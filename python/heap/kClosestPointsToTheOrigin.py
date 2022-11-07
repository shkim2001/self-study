from heapq import *
class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __lt__(self, other):
    return self.distance() > other.distance()

  def distance(self):
    distance = self.x * self.x + self.y * self.y
    return distance

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
  result = []
  minHeap = []
  for i in range(k):
    heappush(minHeap, points[i])
  
  for j in range(k, len(points)):
    point = points[j]
    if point.distance() < minHeap[0].distance():
      heappop(minHeap)
      heappush(minHeap, point)
  
  return minHeap


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()


# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         minHeap = []
#         res = []
#         for point in points:
#             dist = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))
#             heapq.heappush(minHeap, (-dist, point))
#             if len(minHeap) > k:
#                 heapq.heappop(minHeap)
        
#         for i in range(k):
#             res.append(heapq.heappop(minHeap)[1])
#         return res
            

# #         points.sort(key = lambda P: P[0]**2 + P[1]**2)
# #         return points[:k]   
# # #         lst = []
# # #         res = []
# # #         for i in range(len(points)):
# # #             dist = sqrt(points[i][0]**2 + points[i][1]**2)
# # #             lst.append([dist, points[i]])
# # #             lst = sorted(lst)
        
# # #         for j in range(k):
# # #             res.append(lst[j][1])
            
# # #         return res