def pair_with_targetsum(arr, target_sum):
      left = 0
  right = len(arr) - 1
  
  while left < right:
    tempSum = arr[left] + arr[right]
    if tempSum < target_sum:
      left += 1
    elif tempSum > target_sum:
      right -= 1
    else:
      return [left, right]
