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
# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         return sorted(map(lambda x: (x)**2, nums))

# class Solution(object):
#     dict = { 1 : 'I',  4 : 'IV', 5 :  'V', 9 : 'IX', 10 : 'X', 40 : 'XL', 50 : 'L',
#              90 : 'XC', 100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}
#     def intToRoman(self, num):
#         str = ''
#         list = [10, 100, 1000, 10000]   #get the tens/hundreds/thousands place
#         for i in list:
#             if num % i != 0:
#                 str = self.compute(num % i, i/10) + str
#                 num = num - (num % i)
#         return str
#
#     def compute(self, num, lsb):
#         if num in self.dict:
#             return self.dict[num]
#         else:
#             return self.compute(num-lsb, lsb) + self.dict[lsb]

# class Solution(object):
#     def romanToInt(self, s):
#         const_dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#         lst = [const_dct[i] for i in s]
#         res = 0
#         idx = 0
#
#         while idx < len(lst):
#             if idx < len(lst) - 1 and lst[idx] < lst[idx + 1]:
#                 res -= lst[idx]
#                 idx += 1
#             else:
#                 res += lst[idx]
#                 idx += 1
#
#         return res

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         prefix = min(strs, key=len)
#         while not all(s.startswith(prefix) for s in strs):
#             prefix = prefix[:-1]
#         if not prefix:
#             prefix = ""
#         return prefix

# class Solution(object):
#     def letterCombinations(self, digits):
#         if not digits:
#             return []
#
#         mapping = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
#         ans = ['']
#         for d in digits:
#             ans = [comb+choice for comb in ans for choice in mapping[int(d)]]
#         return ans

# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         result = list()
#         nums.sort()
#         start, end = 0, len(nums) - 1
#         while start < end:  # shift start (+1)
#             if start > 0 and nums[start] == nums[start-1]:
#                 start += 1; continue
#             # the following  code is similar to 3Sum
#             while (start + 1) < (end - 1): # shift end (-1)
#                 if end < len(nums)-1 and nums[end] == nums[end+1]:
#                     end -= 1; continue
#                 left = start + 1
#                 right = end - 1
#                 while left < right:
#                     s = nums[start] + nums[left] + nums[right] + nums[end]
#                     if s < target:
#                         left += 1
#                     elif s > target:
#                         right -= 1
#                     else:
#                         result.append([nums[start], nums[left], nums[right], nums[end]])
#                         while left < right and nums[left] == nums[left + 1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right - 1]:
#                             right -= 1
#                         left += 1; right -= 1
#                 end -= 1
#             start += 1; end = len(nums) - 1
#         return result

# if head == None or head.next==None:
#     return head
# first=head
# second=head.next.next
# head=head.next
# head.next=first
# while second and second.next :
#     first.next=second.next
#     temp=second.next.next
#     second.next.next=second
#     second.next=None
#     first=second
#     second=temp
# first.next=second
# return head

# class Solution(object):
#     def reverseKGroup(self, head, k):
#         new = ListNode()
#         new.next = head
#
#         curr = head
#         prev = new
#         last_end = new
#         is_valid = True
#
#         while curr:
#
#             counter = 1
#             checker = curr
#
#             while counter < k:
#                 checker = checker.next
#                 if checker is None:
#                     is_valid = False
#                     break
#                 counter += 1
#
#             if not is_valid:
#                 break
#
#             counter = 0
#
#             while counter < k:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp
#                 counter += 1
#
#             swap_end = last_end.next
#             last_end.next = prev
#             swap_end.next = curr
#             last_end = swap_end
#
#         return new.next

# class Solution(object):
#     def removeDuplicates(self, nums):
#         for i in nums:
#             while i in nums[nums.index(i)+1:]:
#                 nums.remove(i)
#         return len(nums)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        g = len(nums)
        k = 0
        for i in nums:
            if i == val:
                k += 1
        for i in range(0, k):
            nums.remove(val)
        return (g-k)