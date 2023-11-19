"""
My second problem. I am working with python to reinforce my understanding on universal documentation.

LeetCodes question: 

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Pseudo Code:

This one seems simple so we will go ahead and use sort for our function. Sorting both strings and comparring them to eachother to make sure that all letters are used in both strings.
"""

class is_anagram(object):
  def anagram(self, s, t):

    #First we will sort both strings so they appear from a to z

    clean_s = sorted(s)
    clean_t = sorted(t)

    #next it is time to add our if statment to make sure that the strings are now equal to eachother, and if so, return true.

if clean_s == clean_t:

  return True

#if they are not equal to eachother return flase

return False

