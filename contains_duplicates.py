"""
My first problem. I started with python to reinforce my understanding on universal documentation.

LeetCodes question: 

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Pseudo Code:

we are going to use a hash set for this solution. Hash sets are a  collection of objects, Instead of being stored as key value pairs like in hash maps. Both use the hash map data strucute to store data and do not allow duplicate elements to be stored.
"""
#We will first start with the class and function.

class containsDuplicates(object):
  def containsDuplicate(self, nums):

#now we will add pythons set function to make a hash set named seen.

    seen = set()

#next we create our for loop to cycle through our nums array

    for num in nums:

#once we have that we will use an if statment to see if num has already been inserted into the seen hash set and if so will return true and stop looping.

    if num in seen:
      return True

#if the if statement does not happen then we add num to our hash set

    seen.add(num)

#if the for loop is completed then we will finally return False

  return False

  
