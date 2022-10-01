from collections import deque

def is_scheduling_possible(tasks, prerequisites):
      sortedGraph = []

      # TODO: Write your code here
      if tasks <= 0:
            return False

      freq = {}
      pre = {}

      for i in range(tasks):
            freq[i] = 0
            pre[i] = []
      
      for prereq in prerequisites:
            parent, child = prereq[0], prereq[1]
            pre[parent].append(child)
            freq[child] += 1

      queue = deque()
      for key in freq:
            if freq[key] == 0:
                  queue.append(key)
            
      while queue:
            currentNode = queue.popleft()
            sortedGraph.append(currentNode)
            for child in pre[currentNode]:
                  freq[child] -= 1
                  if freq[child] == 0:
                        queue.append(child)
      
      if len(sortedGraph) == tasks:
            return True

      return False


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()