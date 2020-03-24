# 使用分治法策略将一个串行(list)分为两个子串行(sub-lists)
# 本质上是在冒泡排序基础上的递归分治法
# http://data.biancheng.net/view/117.html
def quickSort(arr, left=None, right=None):
  left = 0 if not isinstance(left, (int, float)) else left
  right = len(arr)-1 if not isinstance(right, (int, float)) else right
  if left < right:
    partitionIndex = partition(arr, left, right)
    quickSort(arr, left, partitionIndex - 1)
    quickSort(arr, partitionIndex + 1, right)
  return arr

def partition(arr, left, right):
  pivot = left
  index = pivot + 1
  i = index
  while i <= right:
    if arr[i] < arr[pivot]:
      swap(arr, i, index)
      index += 1
    i += 1
  swap(arr, pivot, index-1)
  return index-1

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]
