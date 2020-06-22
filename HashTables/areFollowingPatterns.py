"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
"""

# found solution one
def areFollowingPatterns(strings, patterns):
  n = len(strings)
  for i in range(n):
    for j in range(i+1,n):
      if strings[i]==strings[j] and patterns[i]!=patterns[j]:
        return False
      if strings[i]!=strings[j] and patterns[i]==patterns[j]:
        return False
  return True
