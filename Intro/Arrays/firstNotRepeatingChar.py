"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

"""

# iterate through string (turn string into list?)
# add characters to a new string
# if that character is not in the set
# return that character
# if no character found
# return - 

# solution 1
def firstNotRepeatingCharacter(s):
  order = []
  counts = {}
  for char in s:
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1
      order.append(char)
  for char in order:
    if counts[char] == 1:
      return char
  return "_"