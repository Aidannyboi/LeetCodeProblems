"""
My third problem. I am working with python to reinforce my understanding on universal documentation.

LeetCodes question: 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Pseudo Code:

For this one we can start with a simple brute foce of nested loops. But that usually increases runtime so we may switch to a hash map.
"""

class Solution(object):
    def twoSum(self, nums, target):
      #first assign a variable that will equal the length of the array nums. We do this so we can create a for loop to loop the whole array.
      x = len(nums)

      #now we will create the loop. This loop will iterate through the entire array EXCEPT for the last integer.
      for i in range(x-1):

        #next we add the secong loop. This one will do the same except in reverse. So the second integer to the last integer.
        for n in range(i + 1, x):

          #compare both intergers from the array. If they equal the target integer, then return borh array locations into a new array. If not go back to line 23.
          if nums[i] + [n] == target:
            return [i, n]
    return[]

#This solution works but it uses 2121 ms to run and uses 14.27 mb to work. Lets try using a hash map.
      
