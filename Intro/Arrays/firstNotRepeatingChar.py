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
s = "abacabad"
def firstNotRepeatingCharacter(s):
  # creating order array
  order = []
  # creating count dictionary
  counts = {}
  # iterate through every char in string
  for char in s:
    # if the char is in the count
    if char in counts:
      # char is key and value goes up one
      counts[char] += 1
    # if char is not in the count
    else:
      # add the char as the key and the value as one
      counts[char] = 1
      # append the char to the order array
      order.append(char)
  # once the for loop ends, for every char in order
  for char in order:
    # if the count value is = 1,
    if counts[char] == 1:
      # return that char
      return char
  # if no value is found, return underscore
  return "_"

firstNotRepeatingCharacter(s)

# solution 2 - fast and weird
# def firstNotRepeatingCharacter(s):
#   for i in s:
#     if s.find(i) == s.rfind(i):
#       return i
#   return "_"

# # solution 3 
# def firstNotRepeatingCharacter(s):
#   for i in range(len(s)):
#     isRepeating = False
#     for j in range(len(s)):
#       if s[i] == s[j] and i != j:
#         isRepeating = True
#     if not isRepeating:
#       return s[i]
#   return "_" 

