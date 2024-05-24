def bubble_sort(arr):
  """
  Bubble sort algorithm.

  Parameters:
    arr: The array to be sorted.

  Returns:
    The sorted array.
  """

  # Iterate over the array, comparing each element with its neighbor.
  for i in range(len(arr) - 1):
    # If the current element is greater than its neighbor, swap them.
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  # Return the sorted array.
  return arr

print(bubble_sort([1,4,58,2,5]))