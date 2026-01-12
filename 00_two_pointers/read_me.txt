What is the Two Pointers Pattern?
The Two Pointers technique involves using two indices (pointers) to iterate over a data structure
(usually an array or a string) to solve problems efficiently by avoiding nested loops.

When to Use Two Pointers?
When you need to find pairs, triplets, or subarrays meeting certain conditions.
When the data is sorted or can be sorted.
When you want to optimize brute force solutions that use nested loops (O(n2)) to linear or
near-linear time (O(n)).

How It Works?
You maintain two pointers that move through the data structure according to certain rules:
One pointer starts at the beginning, the other at the end (common in problems like
finding pairs with a sum).
Or, both pointers start at the beginning, with one moving faster than the other (useful for
sliding window problems).
Move pointers towards each other or forward depending on the problem condition.
                                                                                 
Typical Approach:
Initialize two pointers, left and right.
Check condition based on the current pointers.
                                                                                 
Move pointers accordingly:
If condition not met, move left or right pointer to try to satisfy the condition.
If condition met, record the answer or move pointers to find more solutions.
Repeat until pointers cross or reach the end.

# Problem Name Leetcode
1 Remove Duplicates from Sorted Array
2 Two Sum II - Input Array Is Sorted
3 Move Zeroes
4 Reverse String
5 Container With Most Water
6 Valid Palindrome
7 Squares of a Sorted Array
8 Subarray Product Less Than K
9 Remove Element
10 3 Sum
11 Sort Colors (Dutch National Flag Problem)
12 Longest Substring Without Repeating Characters
13 Minimum Size Subarray Sum
14 Trapping Rain Water LeetCode 42
15 Longest Mountain in Array
