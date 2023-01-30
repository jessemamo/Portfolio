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

# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         g = len(nums)
#         k = 0
#         for i in nums:
#             if i == val:
#                 k += 1
#         for i in range(0, k):
#             nums.remove(val)
#         return (g-k)

# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#
#         for i in range(len(haystack)):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#
#         return -1

# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
#         return min(2 ** 31 - 1, int(str(float(dividend) / float(divisor)).split(".")[0]))

# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         slen = len(s)
#         wlen = len(words[0])
#         conSlen = len(words[0]) * len(words)
#         word_count = collections.Counter(words)
#         res = []
#
#         def getSub(j):
#             return s[j:wlen + j]
#
#         def checkSub(i):
#             remaningCount = word_count.copy()
#             wordCount = 0
#
#             for j in range(i,i+conSlen,wlen):
#                 subs = getSub(j)
#                 if subs in word_count and remaningCount[subs] > 0:
#                     remaningCount[subs] -= 1
#                     wordCount += 1
#                 else:
#                     break
#             return wordCount == len(words)
#
#         for i in range(len(s) - conSlen +1):
#             if getSub(i) in word_count:
#                 if checkSub(i):
#                     res.append(i)
#         return res
#
#
#         solutions = []
#         word_len = len(words[0])
#         sub_len = word_len * len(words)
#         micro_dict = {}
#         for i in range(len(s)):
#             word = s[i:i+word_len]
#             if word in words:
#                 if (i-word_len) in micro_dict:
#                     if ( (i+word_len)-micro_dict[(i-word_len)] ) <=sub_len:
#                         micro_dict[i] = micro_dict[(i-word_len)]
#                     else:
#                         micro_dict[i] = micro_dict[(i-word_len)]+word_len
#                 else:
#                     micro_dict[i] = i
#         inv_map = {}
#         for k, v in micro_dict.items():
#             inv_map[v] = inv_map.get(v, []) + [k]
#         for k, v in inv_map.items():
#             inv_map[k] = max(inv_map[k])+word_len
#
#         for start, end in inv_map.items():
#             temp_dict = {}
#             if end-start ==sub_len:
#                 temp_dict = helper(temp_dict, s[start:end])
#             if temp_dict == words_dict:
#                 solutions.append(start)
#         return solutions

# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         bPoint, n = -1, len(nums)
#         for i in range(n-2,-1,-1):
#             if nums[i] >= nums[i+1]: continue
#             bPoint = i
#             for j in range(n-1,i,-1):
#                 if nums[j] > nums[bPoint]:
#                     nums[j], nums[bPoint] = nums[bPoint], nums[j]
#                     break
#             break
#         nums[bPoint+1:] = reversed(nums[bPoint+1:])

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         i,j=0,len(nums)
#         while(i<j):
#             mid=(i+j)//2
#             if target<nums[0]<nums[mid]:
#                 i=mid+1
#             elif target>=nums[0]>nums[mid]:
#                 j=mid
#             elif nums[mid]<target:
#                 i=mid+1
#             elif nums[mid]>target:
#                 j=mid
#             else:
#                 return mid
#         return -1


# class Solution(object):
#     def searchRange(self,n,t):
#         r=[-1,-1]
#         try:
#             r[0]=n.index(t)
#             n[:]=n[::-1]
#             r[1]=len(n)-(n.index(t)+1)
#         except:
#             return r
#         return r
#
# class Solution(object):
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         cols = collections.defaultdict(set)
#         rows = collections.defaultdict(set)
#         squares = collections.defaultdict(set)
#
#         for r in range(9):
#             for c in range (9):
#                 if board[r][c] == ".": #if empty
#                     continue
#                 if (board[r][c] in rows[r] or
#                         board[r][c] in cols[c] or
#                         board[r][c] in squares[(r//3,c//3)]):
#                     return False
#                     #update the sets
#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[(r//3, c//3)].add(board[r][c])
#         return True

# class Solution(object):
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
#
#         solve_sudoku(board)
#
# def solve_sudoku(grid):
#     row, col = find_empty_cell(grid)
#     if row == -1:
#         return True
#
#     for num in range(1, 10):
#         if is_safe(grid, row, col, num):
#             grid[row][col] = str(num)
#
#             if solve_sudoku(grid):
#                 return True
#
#             grid[row][col] = '.'
#
#     return False
#
# def find_empty_cell(grid):
#     for i in range(9):
#         for j in range(9):
#             if grid[i][j] == '.':
#                 return (i, j)
#
#     return (-1, -1)
#
# def is_safe(grid, row, col, num):
#     # Check if the number is already in the current row
#     for i in range(9):
#         if grid[row][i] == str(num):
#             return False
#
#     # Check if the number is already in the current column
#     for i in range(9):
#         if grid[i][col] == str(num):
#             return False
#
#     # Check if the number is already in the current 3x3 box
#     start_row = row - row % 3
#     start_col = col - col % 3
#     for i in range(3):
#         for j in range(3):
#             if grid[start_row + i][start_col + j] == str(num):
#                 return False
#
#     return True

# class Solution(object):
#     #function that calculate new string based on the last one
#     def getString(self, lastString):
#         currLength = 1
#         curChar = lastString[0:1]
#         string=''
#         for car in lastString[1:]:
#             if car != curChar:
#                 string+=str(currLength)+curChar
#                 curChar=car
#                 currLength = 1
#
#             else:
#                 currLength+=1
#         #this is to insert in the string the set of caracter at the end of last string.
#         string+=str(currLength)+curChar
#         return string
#
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#
#         if n==1:
#             return '1'
#         elif n==2:
#             return '11'
#         else:
#             currentN = 3
#             string = '11'
#             while currentN != n+1:
#                 string = self.getString(string)
#                 currentN+=1
#             return string

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        cur = []
        start = 0
        self.backtracking(candidates, cur, target, results, start)
        return results

    def backtracking(self, candidates, cur, target, results, start):
        if sum(cur) == target:
            results.append(cur[:])
            return
        elif sum(cur) > target:
            return
        for i in range(start, len(candidates)):
            cur.append(candidates[i])


            self.backtracking(candidates, cur, target, results, i)
            cur.pop()
