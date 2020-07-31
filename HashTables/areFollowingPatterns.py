"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
"""

# found solution one
strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]

def areFollowingPatterns(strings, patterns):
  n = len(strings)
  for i in range(n):
    for j in range(i+1,n):
      if strings[i]==strings[j] and patterns[i]!=patterns[j]:
        return False
      if strings[i]!=strings[j] and patterns[i]==patterns[j]:
        return False
  return True

areFollowingPatterns(strings, patterns)

# found very short solution
# added print statements to understand what is happening
strings = ["cat", "dog", "dog"]

patterns = ["a", "b", "b"]

def areFollowingPatterns(strings, patterns):
  # print(set(strings))
  # print(set(patterns))
  # print(set(zip(strings,patterns)))
  if len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns))):
    return True
  else:
    return False

areFollowingPatterns(strings, patterns)

# found solution three
def areFollowingPatterns(strings, patterns):
  pattern_to_string = {}
  string_to_pattern = {}
  for string, pattern in zip(strings, patterns):
    if pattern in pattern_to_string:
        if pattern_to_string[pattern] != string:
            return False
    else:
        pattern_to_string[pattern] = string
    if string in string_to_pattern:
        if string_to_pattern[string] != pattern:
            return False
    else:
        string_to_pattern[string] = pattern
  return True

# found solution four

strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]

def areFollowingPatterns(strings, patterns):
  # hashtable that matches strings to patterns 
  stringToPattern = {}
  # hashtables that matches patters to strings
  patternToString = {}
  # for every item in range of the len of strings
  for i in range(len(strings)):
    # string variable = string you are on. the current iteration
    string = strings[i]
    # pattern variable = string you are on. the current iteration
    pattern = patterns[i]
    # if string is in stringToPatter HT
    if string in stringToPattern.keys():
        # print(stringToPattern.keys())
      # and if pattern does not equal string key
        if(pattern != stringToPattern[string]):
            return False
    # if string is NOT in stringToPattern HT
    else:
        # add it in the HT, and string is key, pattern is value
        stringToPattern[string] = pattern
    # if pattern is in patternToString HT
    if pattern in patternToString.keys():
        # print(patternToString.keys())
        # and if string does not equal pattern (in the patternToString HT)
        if(string != patternToString[pattern]):
          return False
    # otherwise, add it to the HT. pattern key, string value
    else:
        patternToString[pattern] = string
  # once the program iterates through all items it will return true if it has not returned false
  return True

areFollowingPatterns(strings, patterns)