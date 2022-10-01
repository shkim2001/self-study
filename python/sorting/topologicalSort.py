from collections import deque

def topological_sort(vertices, edges):
      sortedOrder = []
      # TODO: Write your code here
      if vertices <= 0:
            return sortedOrder

      children, freq = {}, {}
      
      for i in range(vertices):
            children[i] = []
            freq[i] = 0

      for edge in edges:
            parent, child = edge[0], edge[1]
            children[parent].append(child)
            freq[child] += 1
      
      queue = deque()
      for key in freq:
            if freq[key] == 0:
                  queue.append(key)

      while queue:
            currentNode = queue.popleft()
            sortedOrder.append(currentNode)
            for child in children[currentNode]:
                  freq[child] -= 1
                  if freq[child] == 0:
                        queue.append(child)

      if len(sortedOrder) != vertices:
            return []

      return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
