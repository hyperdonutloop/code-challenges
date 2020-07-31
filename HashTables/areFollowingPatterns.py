"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
"""

# found solution one
# strings = ["cat", "dog", "dog"]
# patterns = ["a", "b", "b"]

# def areFollowingPatterns(strings, patterns):
#   n = len(strings)
#   for i in range(n):
#     for j in range(i+1,n):
#       if strings[i]==strings[j] and patterns[i]!=patterns[j]:
#         return False
#       if strings[i]!=strings[j] and patterns[i]==patterns[j]:
#         return False
#   return True

# areFollowingPatterns(strings, patterns)

# found very short solution
strings = ["cat", "dog", "dog"]

patterns = ["a", "b", "b"]

def areFollowingPatterns(strings, patterns):
  print(set(strings))
  print(set(patterns))
  print(set(zip(strings,patterns)))
  if len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns))):
    return True
  else:
    return False

areFollowingPatterns(strings, patterns)