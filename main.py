# import time
#
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d} : {:02d}' .format(mins,secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
#
#         print('times up')
#
# t = input('How many seconds do you want?:')
#
# countdown(int(t))
# class BinarySearch {
# // Returns index of x if it is present in arr[l..
# // r], else return -1
# int binarySearch(int arr[], int l, int r, int x)
# {
# if (r >= l) {
#     int mid = l + (r - l) / 2;
#
# if (arr[mid] == x)
# return mid;
#
#
# if (arr[mid] > x)
#     return binarySearch(arr, l, mid - 1, x);
#
# return binarySearch(arr, mid + 1, r, x);
# }
#
#
# return -1;
# }
#
#
# public static void main:(String[] args)
# {
# BinarySearch ob = new BinarySearch();
# int arr[] = { 2, 3, 4, 10, 40 };
# int n = arr.length;
# int x = 10;
# int result = ob.binarySearch(arr, 0, n - 1, x);
# if (result == -1)
#     System.out.println("Element not present");
# else
#     System.out.println("Element found at index "
#                        + result);
# }
# }
#
# class Solution:
#     def search(self, nums, target):
#         index = bisect.bisect_left(nums, target)
#         return index if index < len(nums) and nums[index] == target else -1
# class Solution:
#     def search(self, nums, target):
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] < target:
#                 l = mid + 1
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 return mid
#         return -1

# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         return bisect.bisect_left(nums,target)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(map(lambda x: (x)**2, nums))